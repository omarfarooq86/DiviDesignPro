"""
Elegant Themes Blog Monitor
Fetches RSS feed, detects new posts, creates draft markdown files for summary posts.
Run via cron: every 6 hours.
"""
import defusedxml.ElementTree as ET
import urllib.request
import os
import json
from datetime import datetime

RSS_URL = "https://www.elegantthemes.com/blog/feed/"
TRACKING_FILE = "et-posts-tracked.json"
BLOG_DIR = "src/content/blog"
AFFILIATE_ID = "81533"
AFFILIATE_LINK = f"https://www.elegantthemes.com/affiliates/idevaffiliate.php?id={AFFILIATE_ID}"

def fetch_feed():
    """Fetch and parse the Elegant Themes RSS feed."""
    req = urllib.request.Request(RSS_URL, headers={"User-Agent": "DiviDesignPro/1.0"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return ET.fromstring(resp.read().decode('utf-8'))

def load_tracked():
    """Load previously tracked posts."""
    if os.path.exists(TRACKING_FILE):
        with open(TRACKING_FILE, 'r') as f:
            return json.load(f)
    return {"posts": {}, "last_check": None}

def save_tracked(data):
    """Save tracked posts."""
    data["last_check"] = datetime.now().isoformat()
    with open(TRACKING_FILE, 'w') as f:
        json.dump(data, f, indent=2)

def create_draft(title, link, pub_date, description):
    """Create a draft markdown file for a new Elegant Themes post."""
    slug = link.rstrip('/').split('/')[-1]
    # Truncate slug if too long
    if len(slug) > 60:
        slug = slug[:60].rstrip('-')

    draft_path = os.path.join(BLOG_DIR, f"et-{slug}.md")

    if os.path.exists(draft_path):
        return False

    # Extract first paragraph for description
    desc = description[:160].strip() if description else f"Elegant Themes published: {title}"

    content = f"""---
title: '{title} — What It Means for Divi Users'
description: '{desc}'
date: {datetime.now().strftime('%Y-%m-%d')}
category: 'Divi Tips'
featuredImage: '/blog-images/divi-ai-design.jpg'
draft: true
---

Elegant Themes just published a new resource: [{title}]({link}).

[READ THE SUMMARY AND WRITE 3-4 PARAGRAPHS EXPLAINING WHAT THIS POST COVERS, WHY IT MATTERS FOR DIVI USERS, AND HOW TO APPLY IT. ADD YOUR AFFILIATE LINK NATURALLY.]

## Key Takeaways

[LIST 3-5 KEY POINTS FROM THE ORIGINAL POST]

## How to Use This

[1-2 PARAGRAPHS ON PRACTICAL APPLICATION]

## Get Divi

If you want to try this yourself, [get Divi here]({AFFILIATE_LINK}).

---

*This is a summary of [Elegant Themes' original post]({link}). All credit for the original content goes to Elegant Themes.*
"""

    with open(draft_path, 'w', encoding='utf-8') as f:
        f.write(content)

    return True

def main():
    print(f"[{datetime.now().isoformat()}] Checking Elegant Themes blog...")

    tracked = load_tracked()
    feed = fetch_feed()
    new_posts = 0

    for item in feed.findall('.//item'):
        title = item.find('title').text if item.find('title') is not None else ''
        link = item.find('link').text if item.find('link') is not None else ''
        pub_date = item.find('pubDate').text if item.find('pubDate') is not None else ''
        description = item.find('description').text if item.find('description') is not None else ''

        # Skip if already tracked
        post_key = link or title
        if post_key in tracked["posts"]:
            continue

        # Create draft
        if create_draft(title, link, pub_date, description):
            tracked["posts"][post_key] = {
                "title": title,
                "date": pub_date,
                "draft_created": datetime.now().isoformat()
            }
            new_posts += 1
            print(f"  NEW: {title} -> et-{link.rstrip('/').split('/')[-1][:60]}.md")

    save_tracked(tracked)
    print(f"  Done. {new_posts} new draft(s) created.\n")

if __name__ == "__main__":
    main()
