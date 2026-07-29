---
title: 'Divi 5 Global Variables: The Complete Guide for Faster, Consistent Design'
description: 'Master Divi 5 Global Variables (Design Variables) with this hands-on guide. Learn colors, fonts, numbers, fluid sizing, presets, and real freelancer workflows for consistent sites that are easier to maintain.'
date: 2026-07-29
category: 'Divi Tips'
featuredImage: '/blog-images/divi-ai-design.jpg'
---

Global Variables in Divi 5 let you define a design token once — a color, a font, a spacing value — and reuse it everywhere. Change the variable, and **every element referencing it updates across your entire site automatically.**

No hunting through pages. No missed buttons. No inconsistent shades of "almost the right blue."

Here's how they work, how to set them up, and how to use them like a professional Divi freelancer.

## What Are Divi 5 Global Variables?

Divi 5 calls them **Design Variables**. They're reusable values stored at the site level, not inside individual modules. Six types are available:

| Type | What You Store | Example |
|---|---|---|
| **Colors** | Brand palette, backgrounds, borders, text | Primary: `#6c2bd9` |
| **Fonts** | Heading font, body font, accent font | Inter, 600 weight |
| **Numbers** | Spacing, border-radius, font sizes, widths | Section padding: `60px` |
| **Images** | Logos, background patterns | Company logo |
| **Text** | Phone, address, taglines, CTAs | `+92 310 1418307` |
| **Links** | Social profiles, contact page, main CTA | `/contact/` |

This expands the old Divi 4 "Global Colors" into a full **design token system**. It's the single biggest workflow improvement in Divi 5.

## Where to Find the Variable Manager

1. Open the **Divi 5 Visual Builder** on any page
2. Click the **Variable Manager icon** (diamond shape) in the left sidebar
3. The manager opens with tabs for each variable type

The interface shows all your variables organized by category. You can create, edit, delete, and organize them from one place.

## Setting Up Your Color System

### The Four Default Colors

Divi 5 ships with four color variables you can't delete (but can edit):

- **Primary Color** — buttons, links, main accents
- **Secondary Color** — complementary brand color
- **Heading Text Color** — all H1–H6 headings
- **Body Text Color** — paragraphs and body copy

Start by setting these to your brand colors. Then add custom colors as needed.

### Relative Colors (HSL-Based Tints and Shades)

This is where Divi 5's color system shines. You can create **lighter tints, darker shades, and transparent variants** that stay linked to a parent color.

**To create a lighter tint of your primary color:**
1. Click **+ Add Global Color**, name it `Primary Light`
2. Select your Primary Color in the picker
3. Open the **Filter Global Color** panel
4. Adjust **Lightness** to `+20%`

**To create a darker shade:** same process, but set Lightness to `-30%`.

**Why this matters:** Change the base Primary Color later, and every linked tint, shade, and transparent variant updates automatically. You never have to manually recalculate lighter or darker versions again.

### How Many Colors Should You Create?

From experience building 50+ Divi sites, aim for **10-15 color variables**:

- 3-5 brand colors (primary, secondary, accent, dark, light)
- 2-3 text colors (heading, body, muted)
- 2-3 background colors (page, section alt, card)
- 2-3 functional colors (success, error, border)

More than 15 becomes hard to remember. Fewer than 8 usually means you'll need one-off colors later.

## Number Variables for Spacing and Sizing

This is where most people underinvest. Number variables control spacing, border-radius, font sizes, and widths. Setting them up properly makes your site feel **mathematically consistent.**

### The Fluid Sizing Generator

Divi 5 includes a built-in generator for fluid sizing:

1. In the Variable Manager, hover over **Numbers** and click **Generate Fluid Sizing Variables**
2. Choose a token family: Font Size, Spacing, Gap, Radius, or Border Width
3. Pick a scale type:
   - **Fluid** — uses `clamp()` for smooth scaling between mobile and desktop
   - **Fixed Responsive** — separate values per breakpoint
   - **Fixed Single** — one value for all sizes
4. Select a ratio: Major Second (1.125), Major Third (1.25), or Golden Ratio (1.618)

For most projects, I use **Fixed Responsive with Major Third** for spacing, and **Fluid with Major Second** for typography. It creates a natural visual rhythm without any manual math.

### Practical Spacing Scale

Here's the spacing system I use across almost every project:

```
Spacing – XSmall: 10px
Spacing – Small:  20px
Spacing – Medium: 30px
Spacing – Regular: 60px
Spacing – Large:  100px
```

These five values cover section padding, card gaps, module margins, and content spacing. Every module references one of these five numbers — the result is visually consistent spacing across the entire site without measuring anything.

## Applying Variables in Your Designs

1. Open settings for any section, row, column, or module
2. Find the field you want to control (background color, padding, font family)
3. Click the **Dynamic Content icon** (diamond) next to the field
4. Select the variable from the list

The field now references the variable. It's no longer a hard-coded value. Update the variable later, and the change cascades everywhere.

## Variables + Presets: The Full Design System

Variables alone are useful. But paired with Presets, they become a **complete design system.**

Build in this order:

1. **Define Variables** — your design atoms (colors, fonts, spacing)
2. **Create Option Group Presets** — reference variables for specific groups like borders, typography, spacing
3. **Build Element Presets** — full module defaults that stack multiple Option Group Presets
4. **Apply to pages** — override on individual modules only when necessary

**The change flow:** Update a variable → all presets referencing it update → all modules using those presets update.

This three-layer system means you can redesign an entire site by editing 5-10 variables. I've done it on client sites in under an hour.

## Real Freelancer Workflow: How I Use Variables on Every Project

Here's the exact process I follow when starting a new Divi 5 build:

1. **Gather brand assets** — client's logo, brand guide, or existing site colors
2. **Create color variables first** — Primary, Secondary, Dark, Light, and functional colors
3. **Build the relative color chain** — lighter/darker variants linked to each base
4. **Set up the spacing scale** — 5 values using the Fluid Sizing Generator
5. **Define typography variables** — heading font, body font, and font size scale
6. **Add text variables** — client's phone, address, business name for dynamic use
7. **Build Presets on top** — buttons, cards, headings referencing variables
8. **Start designing pages** — every style field references a variable or preset

This takes 30-45 minutes at the start of a project and saves hours of rework later. The first time a client asks to "just try a different shade of blue," you'll understand why this matters.

## Common Mistakes and How to Avoid Them

### Using Vague Names

**Bad:** `Blue 1`, `Blue 2`, `Spacing 1`
**Good:** `Primary Button Background`, `Border – Fields Dark`, `Spacing – Card Gap`

Name variables by their **purpose**, not their value. Six months from now, you won't remember what "Blue 2" was for.

### Creating Too Many Variables

I've seen sites with 40+ color variables. You don't need that many. If you can't explain what a variable does in one sentence, you probably don't need it.

### Not Checking for Static Overrides

If you update a variable and nothing changes on a specific element, that element likely has a **static override** — a manually set value instead of the variable reference. Hover over the field in settings and verify the diamond icon is active.

### Skipping Variables Altogether

The biggest mistake: building an entire site with hard-coded values, then needing to change the brand color across 40 pages manually.

**Spend 30 minutes on variables upfront. It pays for itself on the first revision round.**

## Migrating from Divi 4 Global Colors

If you're coming from Divi 4, your old Global Colors won't automatically become Divi 5 Variables. You'll need to:

1. Note your Divi 4 color values before upgrading
2. Create matching variables in Divi 5's Variable Manager
3. Re-apply them to your key elements and presets

Divi 5's system is significantly more powerful — the migration is worth the effort. Plan for 1-2 hours on a typical site.

## Frequently Asked Questions

### Can I import variables from another Divi 5 site?

Divi 5 doesn't have native variable import/export yet, but variables are bundled into layout JSON when you export. Third-party tools like Divi Assistant support direct variable transfer between sites.

### What happens if I delete a variable that's in use?

Divi warns you. Elements using a deleted variable revert to their static values. Always check where a variable is used before deleting it.

### Can I use CSS functions inside number variables?

Yes. Number variables support `clamp()`, `calc()`, `min()`, `max()`, `vw`, `rem`, `em`, `px`, and `%`. Example: `clamp(1rem, 3vw, 2rem)` creates fluid sizing between 16px and 32px.

### Do variables affect site performance?

No. Variables are resolved at render time into static CSS values. There's zero performance overhead compared to hard-coded values.

### Can clients use variables without breaking things?

Yes — but train them first. Show clients where the Variable Manager is and explain that changing a variable here updates the whole site. Most non-technical clients understand this within 5 minutes.

## The Bottom Line

Divi 5 Global Variables aren't just a renamed version of Global Colors. They're a fundamentally different way to build websites — one where design consistency is automatic and site-wide changes take seconds, not hours.

If you're building sites professionally, variables should be the first thing you set up on every new project. The 30 minutes you spend upfront will save you more time than any other single Divi 5 feature.

## Related Posts

- [Divi 5 Loop Builder: Dynamic Content Made Easy](/blog/divi-5-loop-builder-dynamic-content-made-easy/) — Pair Variables with the Loop Builder for a complete dynamic design system
- [Divi 5 vs Divi 4: What Changed and Which Should You Use?](/blog/divi-5-vs-divi-4-what-changed/) — See how Global Variables compare to Divi 4's limited Global Colors
- [Divi 5 Speed Optimization Tips](/blog/divi-5-speed-optimization-tips/) — Variables are lightweight by design, but speed still matters. Here's the full guide
