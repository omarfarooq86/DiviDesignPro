import json, base64, urllib.request, os

API_KEY = "AQ.Ab8RN6JEavjrCjgv3UXQ33bMOKt-UnDg9Sz7wV6YLDQZSnTlBw"
URL = f"https://generativelanguage.googleapis.com/v1/models/gemini-3.1-flash-lite-image:generateContent?key={API_KEY}"
OUT_DIR = "public/blog-images"

posts = {
    "et-best-wordpress-theme-builders.md": "Side-by-side comparison of 5 WordPress theme builder interfaces (Divi, Elementor, Bricks, Beaver Builder, Gutenberg) on a dark professional background. Each builder represented by a distinct colored card. Modern comparison theme.",
    "et-best-wordpress-themes-for-bloggers.md": "A clean blog layout with a beautiful typography-focused design surrounded by multiple WordPress theme thumbnails. Light, airy, content-focused atmosphere. Writing/blogging theme.",
    "et-the-beauty-of-divi-5s-gradient-variables.md": "A color gradient spectrum flowing through a control panel interface. Multiple gradient swatches (linear, radial, conic) radiating from a central hub. Vibrant colors, dark background.",
    "et-best-variable-fonts-for-web-design-now-in-divi-5.md": "Typography showcase: multiple font styles and weights (thin to bold) displayed as a beautiful typographic specimen poster. Variable font axis sliders. Clean, editorial design style.",
    "et-everything-you-need-to-know-about-workspaces-in-divi-5.md": "Multiple desktop workspaces arranged in a grid, each showing a different tool layout configuration. Organized, productive workspace aesthetic. Clean modern office vibe.",
    "et-exploring-divi-5s-new-text-fill-options-create-text-gradient.md": "Close-up of text with gradient fills and image masks. Words filled with colorful gradients and nature imagery. Creative typography art. Dark background makes fills pop.",
    "et-hover-effects-you-can-create-with-aspect-ratio-and-framing-i.md": "Split composition: left side shows normal images, right side shows the same images with hover effects (zoom, overlay, border animation). Interactive feel. Tech UI aesthetic.",
    "et-how-to-build-better-blog-portfolio-and-product-grids-with-as.md": "Perfectly aligned image grid with consistent aspect ratios. Before/after split showing mismatched vs aligned grids. Clean, geometric, organized layout aesthetic.",
    "et-how-to-create-reusable-border-and-shadow-presets-in-divi-5.md": "Cards and UI elements with different border styles and shadow depths arranged like a design system spec sheet. Minimal, organized, like a style guide catalog.",
    "et-knockout-grids-for-divi-5.md": "Bold grid layout with striking negative space and knockout effects. Modern, architectural grid design. High contrast. Dark background with colored grid elements.",
    "et-part-7-of-mastering-flexbox-building-flexible-button-menu-an.md": "Clean UI showing flexible button rows, menu layouts, and link groups arranged with perfect spacing. CSS Flexbox diagram aesthetic. Developer/designer theme.",
    "et-text-overlapping-image-designs-for-divi-5.md": "Artistic composition where bold typography overlaps and intersects with photographs. Modern magazine-cover style. Creative, edgy, design-forward aesthetic.",
}

for filename, prompt in posts.items():
    slug = filename.replace('.md', '').replace('et-', '')
    out_png = os.path.join(OUT_DIR, f"{slug}.png")
    out_webp = os.path.join(OUT_DIR, f"{slug}.webp")

    if os.path.exists(out_webp):
        print(f"SKIP {slug} (exists)")
        continue

    print(f"Generating: {slug}...")
    data = json.dumps({
        "contents": [{"parts": [{"text": f"Blog featured image 1200x630. {prompt}"}]}],
        "generationConfig": {"responseModalities": ["IMAGE", "TEXT"]}
    }).encode('utf-8')

    req = urllib.request.Request(URL, data=data, headers={"Content-Type": "application/json"})

    try:
        with urllib.request.urlopen(req, timeout=90) as resp:
            result = json.loads(resp.read().decode('utf-8'))

        for part in result['candidates'][0]['content']['parts']:
            if 'inlineData' in part:
                img_data = base64.b64decode(part['inlineData']['data'])
                with open(out_png, 'wb') as f:
                    f.write(img_data)
                print(f"  PNG saved: {len(img_data)} bytes")
                break
    except Exception as e:
        print(f"  ERROR: {e}")

print("\nDone generating! Now run the compression script.")
