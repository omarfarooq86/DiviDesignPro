#!/usr/bin/env python3
"""
Rank tracker for dividesignpro.com.

Checks where the site sits in live Google results for its target keywords and
appends every run to scripts/rank-history.json, so movement is visible over
time without a third-party dashboard.

Why this exists: as of 19 September 2026 the site ranked for nothing at all —
zero keywords in Google's US top 100. That is the baseline. This script is how
you prove movement away from it.

Setup
-----
Get an API password from https://app.dataforseo.com/api-access, then either
export the two variables:

    export DATAFORSEO_LOGIN='you@example.com'
    export DATAFORSEO_PASSWORD='your-api-password'

or copy rank-tracker.env.example to rank-tracker.env and fill it in. The env
file is read automatically and is gitignored.

Usage
-----
    python scripts/rank-tracker.py               # check every target keyword
    python scripts/rank-tracker.py --history     # print history, spend nothing
    python scripts/rank-tracker.py --only lahore # only keywords containing "lahore"
    python scripts/rank-tracker.py --depth 50    # look deeper than the top 20

Cost
----
One SERP request per keyword at roughly $0.002 each, so a full run of the
default ten keywords costs about two cents.
"""

from __future__ import annotations

import argparse
import base64
import json
import os
import sys
import urllib.error
import urllib.request
from datetime import date
from pathlib import Path

HERE = Path(__file__).resolve().parent
HISTORY = HERE / "rank-history.json"
ENV_FILE = HERE / "rank-tracker.env"

API_URL = "https://api.dataforseo.com/v3/serp/google/organic/live/regular"
TARGET_DOMAIN = "dividesignpro.com"

# Market presets. Lahore is a city-level SERP; the US is the main export market.
US = {"location_code": 2840, "language_code": "en"}
LAHORE = {"location_name": "Lahore,Punjab,Pakistan", "language_code": "en"}

# The keywords this site is actually trying to win. Every one was chosen from
# DataForSEO volume/difficulty data rather than guesswork — see the keyword
# strategy note. Divi terms are tracked only to prove the point that they are
# not worth chasing.
TARGETS = [
    {"keyword": "hire wordpress developer", **US},
    {"keyword": "wordpress developer for hire", **US},
    {"keyword": "wordpress maintenance services", **US},
    {"keyword": "wordpress maintenance packages", **US},
    {"keyword": "divi developer", **US},
    {"keyword": "divi expert", **US},
    {"keyword": "web design lahore", **LAHORE},
    {"keyword": "website design lahore", **LAHORE},
    {"keyword": "web development company lahore", **LAHORE},
    {"keyword": "wordpress developer pakistan", **LAHORE},
]


def load_env_file() -> None:
    """Populate os.environ from rank-tracker.env, without overwriting real vars."""
    if not ENV_FILE.exists():
        return
    for raw in ENV_FILE.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        os.environ.setdefault(key.strip(), value.strip().strip("'\""))


def check_keyword(target: dict, depth: int) -> tuple[int | None, float]:
    """Return (absolute rank, cost) for TARGET_DOMAIN on one keyword.

    A rank of None means the domain was not found within `depth` results —
    which is a real result worth recording, not an error.
    """
    login = os.environ.get("DATAFORSEO_LOGIN")
    password = os.environ.get("DATAFORSEO_PASSWORD")
    if not login or not password:
        sys.exit(
            "Missing credentials.\n"
            "Set DATAFORSEO_LOGIN and DATAFORSEO_PASSWORD, or copy\n"
            f"  {ENV_FILE.name}.example -> {ENV_FILE.name}\n"
            "and fill it in. API password: https://app.dataforseo.com/api-access"
        )

    payload = [{"device": "desktop", "depth": depth, **target}]
    request = urllib.request.Request(
        API_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": "Basic "
            + base64.b64encode(f"{login}:{password}".encode()).decode(),
            "Content-Type": "application/json",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(request, timeout=90) as response:
            body = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        sys.exit(f"DataForSEO returned HTTP {exc.code}: {exc.read()[:300]!r}")
    except urllib.error.URLError as exc:
        sys.exit(f"Could not reach DataForSEO: {exc.reason}")

    if body.get("status_code") != 20000:
        sys.exit(f"DataForSEO error: {body.get('status_message')}")

    model = body["tasks"][0]
    cost = float(model.get("cost") or 0)

    if not model.get("result"):
        return None, cost

    for item in model["result"][0].get("items") or []:
        if item.get("type") == "organic" and TARGET_DOMAIN in (item.get("domain") or ""):
            return item.get("rank_absolute"), cost

    return None, cost


def load_history() -> dict:
    if HISTORY.exists():
        return json.loads(HISTORY.read_text(encoding="utf-8"))
    return {"target": TARGET_DOMAIN, "runs": []}


def save_history(history: dict) -> None:
    HISTORY.write_text(json.dumps(history, indent=2) + "\n", encoding="utf-8")


def previous_positions(history: dict, before_date: str) -> dict[str, int]:
    """Most recent recorded position per keyword from runs before `before_date`."""
    previous: dict[str, int] = {}
    for run in history["runs"]:
        if run["date"] >= before_date:
            continue
        for keyword, rank in run["results"].items():
            if rank is not None:
                previous[keyword] = rank
    return previous


def show_history(history: dict) -> None:
    if not history["runs"]:
        print("No runs recorded yet. Run without --history to take the first one.")
        return
    for run in history["runs"]:
        print(f"\n{run['date']}  ({run.get('market', '')})")
        for keyword, rank in run["results"].items():
            print(f"  {rank if rank is not None else '—':>4}  {keyword}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Track dividesignpro.com rankings.")
    parser.add_argument("--history", action="store_true", help="print stored history and exit")
    parser.add_argument("--only", help="only run keywords containing this text")
    parser.add_argument("--depth", type=int, default=20, help="results to inspect (default 20)")
    args = parser.parse_args()

    history = load_history()

    if args.history:
        show_history(history)
        return

    load_env_file()

    targets = TARGETS
    if args.only:
        needle = args.only.lower()
        targets = [t for t in targets if needle in t["keyword"].lower()]
        if not targets:
            sys.exit(f"No target keyword contains {args.only!r}.")

    today = date.today().isoformat()
    previous = previous_positions(history, today)

    print(f"Checking {len(targets)} keyword(s) for {TARGET_DOMAIN} — {today}\n")
    print(f"{'rank':>6}  {'was':>5}  keyword")
    print("-" * 62)

    results: dict[str, int | None] = {}
    total_cost = 0.0
    newly_ranked: list[str] = []

    for target in targets:
        keyword = target["keyword"]
        rank, cost = check_keyword(target, args.depth)
        results[keyword] = rank
        total_cost += cost

        was = previous.get(keyword)
        if rank is None:
            marker = "—"
        else:
            marker = str(rank)
            if was is None:
                newly_ranked.append(keyword)

        delta = ""
        if rank is not None and was is not None and rank != was:
            delta = f"  ({'▲' if rank < was else '▼'}{abs(was - rank)})"

        print(f"{marker:>6}  {was if was is not None else '—':>5}  {keyword}{delta}")

    history["runs"].append(
        {
            "date": today,
            "depth": args.depth,
            "results": results,
            "cost_usd": round(total_cost, 4),
        }
    )
    save_history(history)

    ranked = sum(1 for r in results.values() if r is not None)
    print("-" * 62)
    print(f"{ranked}/{len(targets)} keywords ranking · run cost ${total_cost:.4f}")
    print(f"History: {HISTORY.relative_to(HERE.parent)}")

    if newly_ranked:
        print("\nNewly ranking (first time seen):")
        for keyword in newly_ranked:
            print(f"  #{results[keyword]}  {keyword}")

    if ranked == 0:
        print(
            "\nNothing ranking yet. That matches the September 2026 baseline, so\n"
            "it is expected this early — new pages typically take 8-12 weeks to\n"
            "settle. Re-run monthly and watch this number."
        )


if __name__ == "__main__":
    main()
