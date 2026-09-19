# Backlink Strategy — DiviDesignPro

## Audit: where the profile stands (19 September 2026)

Pulled from the DataForSEO Backlinks API. The short version: **the site has no
earned backlinks at all.**

| Metric | Value |
|---|---|
| Referring domains | 22 |
| Total backlinks | 24 |
| Legitimate referring domains | **0** |
| Overall spam score | 55 |

Every one of the 22 domains falls into one of two auto-generated networks:

**1. A link-selling PBN — 12 domains, dofollow.** Page titles read
"Boost your Google rankings with Premium PBN & Link Building", and the anchor
text is itself an advertisement for paid links: *"High Quality Dofollow
Backlinks DA 50 PA 40 Premium PBN Network Service … Buy Backlinks Online
Cheap"*. Spam scores 60–70. Includes fashionclothingnews.com, uncledspizza.com,
betwinnermirror.com, homesforsaleoldgreenwichct.com.

**2. A "domain report" network — 10 domains, nofollow.** Auto-generated report
and URL-share pages, most sharing the single IP 195.20.19.178. Anchor text is
just the bare domain. Includes quero.party, screenshots.wiki, drjack.world.

Neither was built by hand — the domain was swept up automatically.

### What this means

**This is not what is holding the site back.** Google's spam systems already
ignore links like these, they pass no value, and there is no sign of a manual
action. Disavowing them is cheap insurance and nothing more. Do not expect a
ranking to move because of it.

**The real problem is the opposite one — there is nothing to disavow *for*.**
Zero legitimate referring domains means nothing external vouches for the site,
which is what makes competitive terms like "hire wordpress developer"
(KD 12–23) hard no matter how good the page is. The phases below are the actual
work; the disavow is housekeeping.

A ready-to-submit disavow file is at `disavow.txt`. Submit it via Search Console
→ Indexing → Disavow links. It is reversible.

### Measuring whether any of this works

`scripts/rank-tracker.py` records where the site sits for its target keywords
and appends each run to `scripts/rank-history.json`. The September 2026 baseline
is zero keywords ranking. Run it monthly and watch that number. Setup is two
environment variables — see the header of the script.

---

## Phase 1: Foundation (Week 1 — Free & Fast)

| Platform | Action | Link To |
|---|---|---|
| **Upwork Profile** | Add dividesignpro.com to portfolio | Homepage |
| **LinkedIn Profile** | Add website link, post about new site | Homepage |
| **GitHub Profile** | Link in bio, pin the repo | Homepage |
| **Facebook Page** | Already has divithemesolution — update link | Homepage |
| **Behance/Dribbble** | Create profile, post 3 portfolio screenshots | Portfolio |
| **Medium/Dev.to** | Republish 2 blog posts with canonical | Blog posts |
| **YouTube** | Create channel, link in banner/about | Homepage |

## Phase 2: Authority (Week 2-4)

| Platform | Action | Link To |
|---|---|---|
| **Elegant Themes Community** | Answer Divi questions, link in signature | Blog / Homepage |
| **Reddit r/divi, r/Wordpress** | Answer questions, share blog posts where relevant | Blog posts |
| **Quora** | Answer "How to hire a Divi developer?" etc. | Blog posts |
| **Stack Overflow** | Answer WordPress/Divi questions | Homepage |
| **WPBeginner / WP Tavern** | Comment on relevant articles | Homepage |
| **Upwork Community** | Share expertise, link in profile | Homepage |

## Phase 3: High-Value (Month 2-3)

| Target | How | Value |
|---|---|---|
| **Guest post on Elegant Themes blog** | Submit Divi 5 tutorial | DA 70+ |
| **Guest post on WPExplorer / WPMU DEV** | WordPress performance article | DA 60+ |
| **Podcast appearance** | WP Builds, WP Tavern, Divi Chat | Brand + link |
| **Divi Marketplace** | Submit a free child theme or layout | DA 70+ |
| **Local business directories** | Clutch, GoodFirms, DesignRush | DA 40-60 |

## Phase 4: Content-Led (Ongoing)

| Tactic | Frequency |
|---|---|
| **Publish blog post** → share on social + Reddit + Quora | Weekly |
| **Skyscraper technique** — improve top-ranking Divi articles | Monthly |
| **Broken link building** — find broken Divi resource links, offer yours | Monthly |
| **HARO / SourceBottle** — respond to journalist queries about WordPress | As available |
| **Create a free tool/resource** (Divi speed checklist, Divi 5 migration calculator) | Quarterly |

## Tracking Spreadsheet Columns
- Date | Platform | URL | DA/DR of Platform | Status (Pending/Live) | Notes

## Priority Order
1. Upwork + LinkedIn (already have accounts) — today
2. Medium cross-post (2 posts) — this week
3. Reddit + Quora engagement — ongoing
4. Elegant Themes guest post — submit within 2 weeks
5. Free Divi resource — within 1 month
