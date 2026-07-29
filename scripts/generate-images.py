import json, base64, subprocess, os, re

API_KEY = "AQ.Ab8RN6JEavjrCjgv3UXQ33bMOKt-UnDg9Sz7wV6YLDQZSnTlBw"
BLOG_DIR = "c:/Users/PROBOOK/OneDrive/Desktop/dividesignpro local/dividesignpro-astro/src/content/blog"
OUT_DIR = "c:/Users/PROBOOK/OneDrive/Desktop/dividesignpro local/dividesignpro-astro/public/blog-images"

# Posts to generate images for (skip the one we already did)
posts = {
    "how-to-convert-ai-generated-designs-to-divi-5-layouts.md": "A futuristic split scene: left side shows an AI brain/robot generating a website mockup, right side shows the Divi 5 WordPress builder transforming it into a real site. Bridge of light connecting them. Dark professional background. Clean tech aesthetic.",
    "how-to-hide-a-section-in-divi-5.md": "A clean website layout with one section visibly fading into transparency like a ghost, while other sections remain solid. A toggle switch or eye icon in the corner. Minimalist design, blue theme. Professional WordPress aesthetic.",
    "divi-5-loop-builder-dynamic-content-made-easy.md": "A conveyor belt or assembly line of identical stylish blog cards, each populating with different content (images, titles, dates) automatically. The cards emerge from a single template blueprint. Clean, modern design with blue accents.",
    "divi-5-speed-optimization-tips.md": "A WordPress website with a speedometer showing 98+ score, racing stripes behind it. Lightning bolt symbols. Fast, sleek, performance-themed. Dark background with green and blue highlights showing speed metrics.",
    "divi-5-the-10-questions-every-user-is-asking-right-now.md": "A giant question mark made of smaller question marks, with speech bubbles around it. Each bubble has different tiny icons representing Divi features. Clean, modern design. Blue and white color scheme. Professional look.",
    "how-to-hire-a-divi-developer-on-upwork.md": "A laptop screen showing Upwork profile cards of Divi developers, with one card highlighted and glowing. Rating stars visible. A handshake icon. Professional hiring/recruitment theme. Modern office aesthetic.",
    "how-much-does-a-divi-freelancer-cost.md": "A clean pricing comparison visual with stylized dollar signs and price tags showing different tiers. A calculator and invoices floating. Professional finance/consulting aesthetic. Blue and green color scheme.",
    "divi-5-vs-divi-4-what-changed.md": "Two versions of the same website side by side: left is older/lagacy (Divi 4) with slightly dated design, right is modern sleek (Divi 5) with glowing new features. VS badge in center. Dark background with vibrant accents.",
    "what-is-divi-5-and-why-you-should-upgrade.md": "An upward arrow made of WordPress blocks transforming from old bricks (bottom) into sleek new Divi 5 elements (top). Stars and sparkles around the new elements. Dark background, blue gradient. Modern, aspirational look.",
    "sticky-sidebar-not-working-in-divi-fix.md": "A split website layout: left shows a broken sidebar scrolling away, right shows the fixed version with the sidebar pinned and highlighted. A wrench/spanner icon. Clean, problem-solution visual. Professional blue theme.",
    "divi-5-global-variables-complete-guide.md": "A central hub or control panel radiating colored lines (variables) to identical website elements everywhere. Change one color and all matching elements update. Centralized design system concept. Sleek, modern, dark theme with rainbow accent lines."
}

import urllib.request, urllib.parse, urllib.error
url_base = f"https://generativelanguage.googleapis.com/v1/models/gemini-3.1-flash-lite-image:generateContent?key={API_KEY}"

for filename, prompt in posts.items():
    slug = filename.replace('.md', '')
    out_file = os.path.join(OUT_DIR, f"{slug}-ai.png")
    out_webp = os.path.join(OUT_DIR, f"{slug}-ai.webp")

    if os.path.exists(out_webp):
        print(f"SKIP {slug} (already exists)")
        continue

    print(f"Generating: {slug}...")

    data = json.dumps({
        "contents": [{"parts": [{"text": f"Blog featured image 1200x630. {prompt}"}]}],
        "generationConfig": {"responseModalities": ["IMAGE", "TEXT"]}
    }).encode('utf-8')

    req = urllib.request.Request(url_base, data=data, headers={"Content-Type": "application/json"})

    try:
        with urllib.request.urlopen(req, timeout=90) as resp:
            result = json.loads(resp.read().decode('utf-8'))

        # Extract base64 image
        for part in result['candidates'][0]['content']['parts']:
            if 'inlineData' in part:
                img_data = base64.b64decode(part['inlineData']['data'])
                with open(out_file, 'wb') as f:
                    f.write(img_data)
                print(f"  SAVED PNG: {len(img_data)} bytes")

                # Compress to WebP with Sharp
                try:
                    import sharp
                    sharp(out_file).resize(800, 450, {'fit': 'cover'}).webp({'quality': 80}).toFile(out_webp)
                    sz = os.path.getsize(out_webp)
                    print(f"  COMPRESSED WebP: {sz//1024}KB -> {slug}-ai.webp")
                except Exception as e:
                    print(f"  Sharp error: {e}")
                break
    except Exception as e:
        print(f"  ERROR: {e}")

print("\nDone!")
