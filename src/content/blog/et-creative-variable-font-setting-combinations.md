---
title: '7 Variable Font Combinations for Divi 5 Typography'
description: 'Seven creative variable font setting combinations for Divi 5, with exact axis values for Roboto Flex, Fraunces, Recursive, Inter and more. Copy them straight in.'
date: 2026-08-23
category: 'Divi Tips'
featuredImage: '/blog-images/divi-ai-design.jpg'
tags:
  - 'divi 5 variable fonts'
  - 'divi 5 typography'
  - 'divi 5 fonts'
hasFAQ: true
faqData:
  - question: 'What are variable fonts in Divi 5?'
    answer: 'Variable fonts are single font files with adjustable axes such as weight, width, slant and optical size. Divi 5 exposes those axes as sliders so you can dial in a custom style without loading extra font files.'
  - question: 'Which variable font axes does Divi 5 support?'
    answer: 'Common axes include weight, width, slant, italic, optical size, grade and font-specific axes such as SOFT and WONK on Fraunces or CASL and MONO on Recursive.'
  - question: 'Do variable fonts slow down a website?'
    answer: 'Usually the opposite. One variable font file can replace several static weights, so you load fewer files. Only enable the axes and subsets you actually use.'
  - question: 'What is the difference between weight and grade?'
    answer: 'Weight changes stroke thickness and reflows the text. Grade changes apparent weight without changing the width, so line breaks stay put — useful for dark backgrounds.'
  - question: 'Which variable font is best for body text in Divi?'
    answer: 'Inter and Roboto Flex are safe, highly legible choices for body copy. Save expressive fonts like Fraunces or Bricolage Grotesque for headings.'
  - question: 'How many fonts should a Divi site use?'
    answer: 'Two is usually right — one for headings, one for body. A single variable font can often do both by using different axis settings for each role.'
---

Variable fonts let one font file behave like a dozen. Divi 5 exposes their axes as sliders, so you can dial in a custom weight, width and slant without loading extra files — and usually load *fewer* bytes than a static font stack.

Here are seven combinations with exact axis values you can type straight into Divi 5's typography settings. If you haven't picked a font yet, start with [the best variable fonts now in Divi 5](/blog/et-best-variable-fonts-for-web-design-now-in-divi-5/) and come back for the numbers.

> **TL;DR:** A variable font is one file with adjustable axes — weight, width, slant, optical size, grade, and font-specific ones like Fraunces' WONK. Seven ready-made combinations below, with numbers. Use expressive settings for headings, restrained ones for body copy, and enable only the axes you actually use.

## Why Variable Fonts Are Usually Faster

Counterintuitive but true: loading one variable font can be lighter than loading four static weights, because you're loading one file instead of four.

The catch is that a variable font file is bigger than a *single* static weight. So the maths works in your favour when you need three or more weights, and against you if you genuinely only need Regular. Most designs need three or more. Most designers load six and use three.

Enable only the axes and character subsets you use, and this is a performance win rather than a cost. If you're already deep in a [Divi 5 speed pass](/blog/divi-5-speed-optimization-tips/), consolidating a font stack into one variable file is one of the easier wins on the list.

## Seven Variable Font Combinations

### 1. Google Sans Flex — clean UI headings

- **Weight** 600
- **Width** 105
- **Optical size** 32

A modern, neutral heading style with a fraction of extra width to keep it from feeling cramped at large sizes.

### 2. Science Gothic — high-impact display

- **Weight** 800
- **Width** 130
- **Contrast** low

Wide and heavy. This is a hero-headline setting, not a subheading setting. Use once per page.

### 3. Roboto Flex — dependable body text

- **Weight** 400
- **Width** 100
- **Grade** 0
- **Optical size** 14

The workhorse. Roboto Flex at these values is genuinely hard to fault for body copy, and it has more axes than you'll ever need if you later want to fine-tune.

### 4. Inter — interface and dense text

- **Weight** 450
- **Optical size** 16
- **Slant** 0

Inter at 450 rather than 400 is the trick here. That half-step adds just enough presence for small interface text without looking bold.

### 5. Fraunces — expressive editorial headings

- **Weight** 700
- **SOFT** 50
- **WONK** 1
- **Optical size** 100

WONK is the best-named axis in typography and it does exactly what it sounds like: switches in the quirkier letterform variants. Excellent for editorial headings. Wildly wrong for a bank.

### 6. Recursive — code and technical content

- **Weight** 500
- **CASL** 0
- **MONO** 1
- **Slant** 0

MONO at 1 gives you monospaced output; CASL at 0 keeps it formal rather than casual. Ideal for documentation and code-adjacent content.

### 7. Bricolage Grotesque — contemporary, slightly odd

- **Weight** 600
- **Width** 100
- **Optical size** 24

The current design-Twitter favourite. Distinctive without being difficult, which is a narrow gap to hit.

## Five Rules for Using These Well

1. **Two fonts, maximum.** One for headings, one for body. Often a single variable font handles both with different axis settings for each role.
2. **Expressive for headings, restrained for body.** Fraunces with WONK on for headings, Inter for the paragraphs underneath. Not the reverse. Never the reverse.
3. **Use Grade, not Weight, on dark backgrounds.** Grade changes apparent weight without changing width, so your line breaks stay put. Light text on dark looks heavier than it is; a slight negative grade corrects it without reflowing the paragraph.
4. **Respect optical size.** It exists because type designed for 14px shouldn't have the same proportions as type at 100px. Setting it correctly is close to free quality.
5. **Store the values as variables.** Put your axis settings in [Divi 5's Variable Manager](/blog/divi-5-global-variables-complete-guide/) so a typography change is one edit rather than forty.

That last point is the one that separates a font experiment from a design system. And once your typography values live in variables, [wrapping them into stacked presets](/blog/et-how-to-stack-nest-mix-and-match-presets-in-divi-5/) means a heading style change propagates site-wide in one click.

## My Take: Variable Fonts Make It Easier to Ruin a Site

Here's my one strong opinion: **variable fonts give you enough rope to hang the whole design, and most people use all of it.**

I've built over 100 Divi sites and typography is where enthusiasm does the most damage. Static fonts had a natural limit — you loaded Regular, Bold, maybe Light, and that was your palette. Constraint by inconvenience.

Variable fonts remove that constraint entirely. Now every heading can have its own weight, width and slant, and I've inherited sites where they did: H1 at width 130, H2 at width 92, H3 back at 108, no two headings related to each other, the whole page vibrating slightly.

The discipline that replaces the old constraint is simple: **pick your axis values once, per role, and don't tune them per element.** Three heading levels, three sets of values, saved as variables. If a specific heading "needs" different width, the problem is the heading's length, not the font.

Use the expressive axes exactly where the design needs a moment — a hero, a pull quote, a section marker. Everywhere else, boring is correct.

## Straight Answers

**What are variable fonts in Divi 5?**
Single font files with adjustable axes — weight, width, slant, optical size — exposed as sliders in Divi's typography settings.

**Which axes does Divi 5 support?**
Weight, width, slant, italic, optical size, grade, plus font-specific ones like Fraunces' SOFT and WONK or Recursive's CASL and MONO.

**Do they slow a site down?**
Usually the opposite — one file can replace several static weights. Enable only the axes and subsets you use.

**Weight vs grade?**
Weight changes thickness and reflows text. Grade changes apparent weight without changing width, so line breaks stay put.

**Best variable font for body text?**
Inter or Roboto Flex. Keep Fraunces and Bricolage Grotesque for headings.

**How many fonts should a Divi site use?**
Two. Often one variable font can cover both roles.

## The Last Word

Copy the numbers above, drop them into [Divi 5's](https://www.elegantthemes.com/affiliates/idevaffiliate.php?id=81533) typography panel, and you have seven starting points that already work. Adjust from there rather than from zero.

Then save your final values as variables and stop touching them. The sites with the best typography aren't the ones using the most axes — they're the ones where every heading agrees with every other heading.

If your type is fighting itself and you'd rather someone else referee, [I do that](#contact). I will also almost certainly turn WONK on somewhere, and I regret nothing.

---

*This is a summary of [Elegant Themes' original post, "Creative Variable Font Setting Combinations"](https://www.elegantthemes.com/blog/divi-resources/creative-variable-font-setting-combinations). All credit for the original content goes to Elegant Themes.*
