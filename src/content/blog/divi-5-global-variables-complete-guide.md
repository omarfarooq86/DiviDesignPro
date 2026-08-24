---
title: 'Divi 5 Global Variables: The Complete Guide (2026)'
description: 'Master Divi 5 Global Variables — colours, fonts, numbers, relative colours, fluid sizing and presets. The design token workflow that lets you restyle a whole site in minutes.'
date: 2026-07-29
updated: 2026-08-24
category: 'Divi Tips'
featuredImage: '/blog-images/divi-5-global-variables-complete-guide-ai.webp'
tags:
  - 'divi 5 global variables'
  - 'divi design variables'
  - 'divi 5 design system'
hasFAQ: true
faqData:
  - question: 'What are Divi 5 Global Variables?'
    answer: 'Reusable design tokens stored at site level rather than inside modules. Six types are available — colours, fonts, numbers, images, text and links. Change the variable and every element referencing it updates.'
  - question: 'Where is the Variable Manager in Divi 5?'
    answer: 'Open the Visual Builder on any page and click the Variable Manager icon, the diamond shape in the left sidebar. It opens with a tab for each variable type.'
  - question: 'How many colour variables should I create?'
    answer: 'Ten to fifteen for a typical site — three to five brand colours, two to three text colours, two to three backgrounds and two to three functional colours. Above fifteen you stop remembering what they are for.'
  - question: 'Do Global Variables slow down a Divi site?'
    answer: 'No. Variables resolve at render time into static CSS values, so there is no runtime overhead compared with hard-coded values.'
  - question: 'Do Divi 4 Global Colors convert to Divi 5 variables automatically?'
    answer: 'No. You need to note your Divi 4 colour values, recreate them as variables in the Variable Manager, and reapply them to key elements and presets. Budget one to two hours on a typical site.'
  - question: 'What happens if I delete a variable that is in use?'
    answer: 'Divi warns you first. Any element using the deleted variable falls back to its last static value. Check where a variable is used before removing it.'
---

Global Variables in Divi 5 let you define a design token once — a colour, a font, a spacing value — and reuse it everywhere. Change the variable, and **every element referencing it updates across your entire site.**

No hunting through pages. No missed buttons. No four slightly different blues that were all meant to be the brand colour.

> **TL;DR:** Six variable types, managed in the **Variable Manager** (the diamond icon). Set up **colours with Relative Colors** for linked tints and shades, then a **five-value spacing scale** with the Fluid Sizing Generator, then build presets on top. Thirty minutes at the start of a project; a site you can restyle in ten. Name variables by purpose, never by value.

## What Divi 5 Global Variables Actually Are

Divi 5 calls them **Design Variables**. They're reusable values stored at the site level, not inside individual modules. Six types:

| Type | What you store | Example |
|---|---|---|
| **Colors** | Brand palette, backgrounds, borders, text | Primary: `#6c2bd9` |
| **Fonts** | Heading font, body font, accent font | Inter, 600 weight |
| **Numbers** | Spacing, border-radius, font sizes, widths | Section padding: `60px` |
| **Images** | Logos, background patterns | Company logo |
| **Text** | Phone, address, taglines, CTAs | `+1 (307) 445-3714` |
| **Links** | Social profiles, contact page, main CTA | `/contact/` |

This expands Divi 4's "Global Colors" into a full **design token system**, and it's the single biggest workflow change in Divi 5 — more consequential day to day than any of the new layout features. [What else changed between Divi 4 and Divi 5](/blog/divi-5-vs-divi-4-what-changed/) puts it in context.

## Where to Find the Variable Manager

1. Open the **Divi 5 Visual Builder** on any page
2. Click the **Variable Manager icon** (diamond shape) in the left sidebar
3. The manager opens with tabs for each variable type

Everything is created, edited, renamed and deleted from this one place.

## Setting Up Your Colour System

### The Four Defaults

Divi 5 ships with four colour variables you can't delete but can edit:

- **Primary Color** — buttons, links, main accents
- **Secondary Color** — complementary brand colour
- **Heading Text Color** — all H1–H6
- **Body Text Color** — paragraphs and body copy

Set these to the client's brand colours first, then add your own.

### Relative Colors (HSL Tints and Shades)

This is the part of the colour system worth learning properly. You can create **lighter tints, darker shades and transparent variants** that stay linked to a parent colour.

To make a lighter tint of your primary:

1. Click **+ Add Global Color** and name it `Primary Light`
2. Select your Primary Color in the picker
3. Open the **Filter Global Color** panel
4. Set **Lightness** to `+20%`

For a darker shade, same process with Lightness at `-30%`.

**Why it matters:** change the base Primary Color later and every linked tint, shade and transparent variant recalculates. You never hand-derive a hover state again — and hover states are exactly where colour drift usually starts.

Gradients get the same treatment: [gradient variables](/blog/et-the-beauty-of-divi-5s-gradient-variables/) can be defined once and referenced across the site.

### How Many Colours?

From building over 100 Divi sites, aim for **10–15 colour variables**:

- 3–5 brand colours (primary, secondary, accent, dark, light)
- 2–3 text colours (heading, body, muted)
- 2–3 backgrounds (page, alternate section, card)
- 2–3 functional (success, error, border)

More than 15 and you stop remembering them. Fewer than 8 and you'll be inventing one-off colours by page four.

## Number Variables for Spacing and Sizing

This is where nearly everyone underinvests, and it's the section to read twice. Number variables control spacing, border-radius, font sizes and widths — the values that make a site feel **mathematically consistent** rather than merely tidy.

### The Fluid Sizing Generator

Divi 5 includes a generator for this:

1. In the Variable Manager, hover over **Numbers** and click **Generate Fluid Sizing Variables**
2. Choose a token family: Font Size, Spacing, Gap, Radius or Border Width
3. Pick a scale type:
   - **Fluid** — uses `clamp()` for smooth scaling between mobile and desktop
   - **Fixed Responsive** — separate values per breakpoint
   - **Fixed Single** — one value everywhere
4. Select a ratio: Major Second (1.125), Major Third (1.25) or Golden Ratio (1.618)

On most projects I use **Fixed Responsive with Major Third** for spacing and **Fluid with Major Second** for typography. That gives a visible rhythm with no manual arithmetic, and typography that scales without a breakpoint jump.

### A Spacing Scale That Works

The five values I use on almost every project:

```
Spacing – XSmall:   10px
Spacing – Small:    20px
Spacing – Medium:   30px
Spacing – Regular:  60px
Spacing – Large:   100px
```

Five numbers cover section padding, card gaps, module margins and content spacing. Every module references one of them. The result is consistent spacing across an entire site without measuring anything, and — more usefully — without *deciding* anything. Fewer choices is why it's faster.

## Applying Variables

1. Open settings for any section, row, column or module
2. Find the field you want to control — background colour, padding, font family
3. Click the **dynamic content icon** (diamond) next to the field
4. Pick the variable

That field now references the variable rather than holding a value. Update the variable and the change cascades.

## Variables Plus Presets: The Full System

Variables alone are useful. With presets they become a **design system**. Build in this order:

1. **Define variables** — your atoms: colours, fonts, spacing
2. **Create option group presets** — reference variables for one group at a time: borders, typography, spacing
3. **Build element presets** — full module defaults that stack option group presets
4. **Apply to pages** — override on an individual module only when there's a real reason

**The change flow:** update a variable → every preset referencing it updates → every module using those presets updates.

That three-layer structure is what lets you redesign a site by editing five to ten variables. I've done it on client sites in under an hour. [How presets stack, nest and mix](/blog/et-how-to-stack-nest-mix-and-match-presets-in-divi-5/) covers the combinations, and [reusable border and shadow presets](/blog/et-how-to-create-reusable-border-and-shadow-presets-in-divi-5/) is the clearest worked example of the option-group idea.

## The Workflow I Use on Every Project

1. **Gather brand assets** — logo, brand guide, or the existing site's colours
2. **Create colour variables** — primary, secondary, dark, light, functional
3. **Build the relative colour chain** — tints and shades linked to each base
4. **Set the spacing scale** — five values via the Fluid Sizing Generator
5. **Define typography variables** — heading font, body font, size scale
6. **Add text variables** — phone, address, business name for dynamic reuse
7. **Build presets on top** — buttons, cards, headings, all referencing variables
8. **Start designing** — every style field points at a variable or a preset

Thirty to forty-five minutes at the start. The first time a client asks to "just try a slightly different blue," it pays for itself with change to spare.

## My Take: Everyone Sets Up Colour Variables and Stops — the Spacing Scale Is the One That Shows

Here's my one strong opinion: **number variables matter more than colour variables, and almost nobody builds them. Inconsistent spacing is what makes a site look amateur, and unlike colour, nobody can tell you why.**

I've built over 100 Divi sites and audited plenty more. When I open someone else's Divi build, the colours are nearly always fine — there's a brand guide, the hex codes got pasted in, and even if they're hard-coded they're at least *the same*. Then I check section padding and find `60px`, `65px`, `70px`, `4rem`, `55px` and one section at `100px` because it "needed more room."

None of those are wrong individually. Collectively they're the reason the site feels slightly off in a way the client can't articulate. They'll say it looks "a bit unpolished" or "not quite like the mockup," and they won't say "your vertical rhythm is inconsistent," because nobody outside this field talks like that. So the feedback comes back as vague dissatisfaction, and vague dissatisfaction is the most expensive kind — you can't fix what nobody can name.

Colour drift, by contrast, gets *noticed and reported*. Two blues on one page is visible, someone flags it, you fix it in five minutes. The bug that gets reported is not the dangerous bug.

There's a second reason spacing variables earn more than colours: they remove decisions. When padding is a free-text field, every section is a small judgement call, and after forty sections you've made forty inconsistent judgements while tired. When padding is a dropdown with five entries, you pick the closest one and move on. **The value isn't only that the values match — it's that you stopped choosing.** That's where the speed comes from, and it's why the spacing scale saves me more time than the colour palette does.

So my rule: if you only have fifteen minutes to set up variables, spend ten on **five spacing values and a type scale** and five on colours. Colour inconsistency is a bug you'll catch. Spacing inconsistency is a texture you'll ship.

## Common Mistakes

### Vague names

**Bad:** `Blue 1`, `Blue 2`, `Spacing 1`
**Good:** `Primary Button Background`, `Border – Fields Dark`, `Spacing – Card Gap`

Name by **purpose**, not value. In six months you won't remember what "Blue 2" was for, and if the brand goes green, `Blue 2` becomes actively misleading.

### Too many variables

I've opened sites with 40+ colour variables. If you can't say what a variable is for in one sentence, delete it.

### Not checking for static overrides

Update a variable and one element doesn't change? It has a **static override** — a manually set value where the reference should be. Hover the field and check the diamond icon is active.

### Skipping variables entirely

The big one: building the whole site with hard-coded values, then being asked to change the brand colour across 40 pages by hand. Thirty minutes up front beats a lost afternoon on the first revision round.

## Migrating from Divi 4 Global Colors

Divi 4 Global Colors don't automatically become Divi 5 variables. You'll need to:

1. Note your Divi 4 colour values before upgrading
2. Recreate them as variables in the Variable Manager
3. Reapply them to key elements and presets

Budget 1–2 hours on a typical site. Do this as part of [the wider Divi 5 upgrade](/blog/what-is-divi-5-and-why-you-should-upgrade/) rather than as a separate job — you're already in there, and the plugin audit in that guide is the step that actually carries risk.

## Straight Answers

**What are they?**
Site-level design tokens in six types: colours, fonts, numbers, images, text, links.

**Where's the Variable Manager?**
Visual Builder, left sidebar, diamond icon.

**How many colours?**
10–15. Above that you lose track.

**Performance cost?**
None. They resolve to static CSS at render.

**Can I import variables between sites?**
No native import/export yet, though variables travel inside exported layout JSON. Some third-party tools handle direct transfer.

**Can I use `clamp()` in a number variable?**
Yes — `clamp()`, `calc()`, `min()`, `max()`, plus `vw`, `rem`, `em`, `px` and `%`.

**What if I delete one in use?**
Divi warns you; affected elements fall back to their static values.

**Can clients touch them?**
Yes, with five minutes of training. Show them the Variable Manager and explain that a change here is site-wide.

## The Last Word

Divi 5 Global Variables aren't renamed Global Colors. They're a different way to build: consistency becomes automatic, and a site-wide restyle becomes a ten-minute job instead of an afternoon of find-and-replace.

Set them up first on every project. Colours, then — more importantly — five spacing values and a type scale. Then build presets on top and let every module reference the system rather than holding its own opinions.

[Divi 5](https://www.elegantthemes.com/affiliates/idevaffiliate.php?id=81533) includes all of this with an active licence, no addon required. If you've inherited a site with hex codes in forty modules and you'd like it converted to a variable system properly, [that's a well-spent day](#contact).

## Related Reading

- [Divi 5 Loop Builder](/blog/divi-5-loop-builder-dynamic-content-made-easy/) — what your loop cards should reference
- [How to Stack, Nest and Mix Presets in Divi 5](/blog/et-how-to-stack-nest-mix-and-match-presets-in-divi-5/) — the layer that sits on top of variables
- [Divi 5 vs Divi 4: Every Real Difference](/blog/divi-5-vs-divi-4-what-changed/) — how this compares with Divi 4's Global Colors
