---
title: 'Divi 5 Text Fill: Gradient, Image and Transparent Text'
description: 'Divi 5 text fill options let you build gradient headings, image-masked text and outlined lettering natively. Every Fill Type, stroke control and the legibility rules that matter.'
date: 2026-07-30
updated: 2026-08-23
category: 'Divi Tips'
featuredImage: '/blog-images/exploring-divi-5s-new-text-fill-options-create-text-gradient.webp'
tags:
  - 'divi 5 text fill'
  - 'divi 5 gradient variables'
  - 'divi 5 typography'
hasFAQ: true
faqData:
  - question: 'Where is the Fill Type setting in Divi 5?'
    answer: 'Open a Heading module, go to the Design tab, and find the relevant text option group — Heading Text, or a level-specific group such as Heading Text H1. Fill Type sits inside it.'
  - question: 'What Fill Type options does Divi 5 offer?'
    answer: 'Four: None keeps the normal text colour, Gradient fills letters with a gradient, Image fills letters with a photo, and Transparent removes the fill for hollow lettering.'
  - question: 'How do you fill text with an image in Divi 5?'
    answer: 'Set Fill Type to Image, choose the image, then adjust its position so the most recognisable part of the photo sits inside the letterforms. Use large, bold type.'
  - question: 'Can you use a text stroke without a transparent fill?'
    answer: 'Yes. Strokes combine with any fill type and are most useful over busy imagery or high-contrast backgrounds. Stroke width and stroke colour are the two controls.'
  - question: 'What font works best for image-filled text?'
    answer: 'A heavy, tightly spaced typeface. Thin fonts do not expose enough surface area for the image to register, so the effect reads as noise rather than a photo.'
  - question: 'How do you reuse a gradient across headings and backgrounds?'
    answer: 'Right-click the gradient field and choose Convert to Variable, then name it by role. The same variable then works on heading fills, button backgrounds and section backgrounds.'
---

Divi 5 moved text effects that used to require Photoshop into the Visual Builder. Gradient fills, image fills, transparent fills and text strokes are all native settings now — and the text stays editable text, not an exported PNG.

The control you're looking for is **Fill Type**, and everything else appears only after you change it from the default.

> **TL;DR:** **Heading** module → **Design** tab → **Heading Text** (or **Heading Text H1**) → **Fill Type**. Four options: **None**, **Gradient**, **Image**, **Transparent**. Stroke width and colour work with any fill. Image fills need heavy, tightly spaced type. One filled heading per page.

## The Four Fill Types

| Fill Type | What it does |
|---|---|
| **None** | Default — keeps the normal text colour |
| **Gradient** | Fills the letters with a gradient |
| **Image** | Fills the letters with an image |
| **Transparent** | Removes the fill for hollow lettering, usually with a stroke |

These live in text option groups, so they're available anywhere Divi surfaces those text controls — heading groups and other module text groups alike.

## Gradient Fill

1. Set **Fill Type** to **Gradient**. Gradient controls appear below.
2. Build with colour stops — click the bar to add a stop, drag to reposition, edit each stop's colour.
3. Set **Gradient Type**: **Linear**, **Circular**, **Elliptical** or **Conical**.
4. Adjust direction or position, which varies by the type you picked.

Divi 5's gradient picker consolidates everything in one panel and behaves more like the colour picker, exposing gradient options and variables together. Gradients are now a unified field, so they copy, paste, extend, inspect, find, replace and reuse cleanly.

**Start with Linear for headings.** Colour movement stays readable and predictable across one or more lines, which matters because a headline that wraps to three lines will do strange things under a conical gradient.

**A worked example — SaaS hero on a near-black background:** two stops, brand green to deep blue pulled from the logo, positions tuned until the blend balanced. Linear, top to bottom. The lower stop was **lightened slightly** so the bottom of the letters didn't merge into the dark section behind them.

That last adjustment is the whole craft of gradient text in one move. The gradient looked correct in isolation and disappeared in context.

## Image Fill

1. **Fill Type** → **Image**. Image controls appear.
2. Select an image, then adjust how it sits within the letterforms.
3. Position it so the most recognisable part of the photo lands inside the text.

**Worked example — travel editorial:** two words, two different image fills. SUMMER filled with a green alpine landscape, WINTER with a cooler blue forest. That's a design that used to mean masking in Photoshop, exporting a PNG, and re-exporting every time the copy changed. Now the words remain editable.

Step 3 is where this succeeds or fails. Letters cover maybe 40% of their bounding box, so most of your photo is discarded — you're choosing which fragments survive.

## Transparent Fill and Text Stroke

**Fill Type** → **Transparent** gives hollow letters. Two stroke controls: **stroke width** and **stroke colour**. Together they produce outlined letters with see-through interiors.

Strokes aren't tied to Transparent. They combine with **any** fill type, and they're most useful over busy imagery or high-contrast backgrounds.

**Worked example — readability over a busy photo (an espresso machine):**

1. Add a dark gradient overlay to the section background, fading roughly **50% → 30% opacity** — enough to calm the highlights without hiding the subject.
2. Heading **Fill Type** → **Gradient**, using a warm off-white matched to the photo.
3. Add a thin stroke: brand orange, **1px**.

The stroke colour matching the button colour is the detail worth stealing. It makes the stroke read as brand styling rather than as a legibility patch — which is exactly what it is.

**Mixed fills in one design:** FRESH with an **Image** fill (leaf texture inside solid letters), LEAVES with **Transparent** fill and a white **Stroke**. Each word is a **separate Heading module**, because Fill Type and Stroke are per-module settings. If you want two words treated differently, you need two modules.

## Save the Gradient as a Variable

Don't rebuild stops every time.

**Fastest route:** build a gradient on any element, right-click the gradient field, choose **Convert to Variable**, and name it by role — **Brand Gradient**, not "Green to Blue."

**Alternative:** **Variable Manager** → **Gradients** category → add a new **Global Gradient**.

To use it in text: Heading module → **Fill Type** → **Gradient** → select the saved variable instead of rebuilding stops.

The same variable then works on heading fills, button backgrounds, section backgrounds and footer treatments. Edit the variable and every element referencing it updates. That's the case for [gradient variables](/blog/et-the-beauty-of-divi-5s-gradient-variables/) in full, and it's especially valuable for seasonal campaigns and product launch pages where the gradient changes but the layout doesn't.

## Legibility Rules

**Image fills need large, bold type.** Thin fonts don't expose enough surface area for the image to register. Use a heavy, tightly spaced typeface — this is a real constraint, not a preference.

**Choose images with strong contrast and a clear subject.** Too dark, too busy or low contrast becomes visual noise inside the letters.

**Keep strokes subtle.** Thin sharpens edges. Heavy crowds the letterforms and looks messy.

**Watch gradient stops against the section background** so letters don't vanish, as in the SaaS example above.

**Be selective.** One filled heading polishes a page. Several competing ones look noisy. Let a single heading carry the effect and keep nearby text plain.

Use text fills when a hero needs a stronger brand moment, an editorial layout needs a focal point, a heading over a busy image needs a stroke, a campaign needs a reusable gradient, or a single word needs emphasis.

Hold back when the heading is small or body-sized, the surrounding design is already busy, the image fill hurts readability, or the effect doesn't tie to brand, image or message.

For pairing these with axis settings, [text stroke, text fill and variable fonts work well together](/blog/et-creative-variable-font-setting-combinations/) — a heavier weight gives an image fill more surface to work with.

## My Take: This Feature Has No Accessibility Story Yet

Here's my one strong opinion: **gradient and image-filled text is a legibility gamble that Divi gives you no tools to check, and the documentation doesn't acknowledge the gap.**

I've built over 100 Divi sites and I've read every published guide to this feature. Every one of them handles readability visually — "watch your stops," "pick a high-contrast image," "keep the stroke thin." All correct. None of them give you a contrast-ratio target, a WCAG reference, or guidance on a fallback colour.

That's a real gap, because **contrast ratio is not a visual judgement, it's a number.** Solid text has one text colour, so you measure it against the background and you're done. Gradient text has a *different* contrast ratio at every point along the gradient. Image-filled text has a different one at every pixel. The espresso-machine example above passes at the top of the letters and might fail at the bottom, and nothing in the builder will tell you.

So my working rule: **measure the worst point, not the average.** Sample the lightest region of your gradient, or the lightest region of the photo appearing inside the letters, and check that against the background. If the worst point fails, the heading fails — a visitor with low vision doesn't get to read the parts that happen to pass.

The practical consequence is that these effects belong on **large display type only**, where WCAG's threshold is more forgiving and the letterforms are big enough that a stroke actually helps. On anything approaching body size, use a solid colour. Not because it looks worse — because you can verify it.

None of this makes the feature bad. It makes it a feature with a sharp edge that the marketing doesn't mention.

## Straight Answers

**Where is Fill Type?**
Heading module → Design tab → Heading Text (or Heading Text H1) → Fill Type.

**What are the options?**
None, Gradient, Image, Transparent.

**How do you fill text with an image?**
Fill Type → Image, choose the image, position it so the recognisable part sits inside the letters. Use bold type.

**Can strokes work without Transparent fill?**
Yes — strokes combine with any fill type, and help most over busy imagery.

**Best font for image fills?**
Heavy and tightly spaced. Thin fonts don't give the image enough surface.

**How do you reuse a gradient?**
Right-click the gradient field → Convert to Variable → name it by role.

## The Last Word

Four Fill Types, two stroke controls, and a workflow that used to involve Photoshop and a re-export every time the copy changed. That's a genuine improvement, and gradient variables make it reusable across headings and backgrounds alike.

Then apply the constraints honestly: one filled heading per page, large type only, subtle strokes, and check the *worst* point of your gradient rather than how it looks at a glance.

[Divi 5](https://www.elegantthemes.com/affiliates/idevaffiliate.php?id=81533) gives you the effects. Restraint and a contrast checker are still your department. If you want a hero heading that's both striking and measurably legible, [that's a fun forty minutes](#contact).

---

*This is a summary of [Elegant Themes' original post, "Exploring Divi 5's New Text Fill Options (Create Text Gradients & Image Masks)"](https://www.elegantthemes.com/blog/divi-resources/exploring-divi-5s-new-text-fill-options-create-text-gradients-image-masks). All credit for the original content goes to Elegant Themes.*
