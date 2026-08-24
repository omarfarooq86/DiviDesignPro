---
title: 'Divi 5 Flexbox: Responsive Columns Without CSS Grid'
description: 'Build responsive columns in Divi 5 with Flexbox instead of CSS Grid. Column Class, Layout Wrapping and Gap explained, plus per-breakpoint reflow with no media queries.'
date: 2026-08-23
category: 'Divi Tips'
featuredImage: '/blog-images/divi-ai-design.jpg'
tags:
  - 'divi 5 flexbox'
  - 'divi responsive design'
  - 'divi 5 tutorial'
hasFAQ: true
faqData:
  - question: 'How do you create responsive columns in Divi 5 without CSS Grid?'
    answer: 'Use Column Class to set each column width as a fraction, then enable Layout Wrapping set to Wrap. Columns sit side by side until they no longer fit, then wrap to the next line.'
  - question: 'What is Column Class in Divi 5?'
    answer: 'Column Class sets a column width basis as a fraction — Fullwidth, 3/4, 2/3, 1/2, 1/3, 1/4, 1/6, or No Column Class — instead of a fixed pixel width.'
  - question: 'Should I use Flexbox or CSS Grid in Divi 5?'
    answer: 'Use Flexbox for card grids, sidebars and feature rows, which is most layouts. Use CSS Grid for true two-dimensional layouts where rows and columns must both align.'
  - question: 'Do I still need margins for spacing in Divi 5 Flexbox?'
    answer: 'Mostly no. Use Horizontal and Vertical Gap on the container instead. Keep margin for one-off offsets or intentional overlaps.'
  - question: 'Can columns reorder on mobile in Divi 5?'
    answer: 'Yes, using Display Order per breakpoint. But test keyboard focus and reading flow, because visual reordering does not change the document order.'
  - question: 'Do I need media queries for responsive Divi 5 columns?'
    answer: 'No. Set a different Column Class per breakpoint and one structure reflows across desktop, tablet and phone without media queries or duplicated content.'
---

You don't need CSS Grid for most responsive layouts in Divi 5. Two settings — **Column Class** and **Layout Wrapping** — handle card grids, sidebars and feature rows with a faster, more visual workflow.

CSS Grid is the right tool for true two-dimensional layouts, where rows *and* columns must align to each other. That's rarer than people think. Most of what we build is a row of things that should wrap nicely on a phone, and Flexbox eats that for breakfast.

> **TL;DR:** Set **Column Class** to a fraction (1/2, 1/3, 1/4) to size each column, then enable **Layout Wrapping > Wrap** so columns flow onto a new line when they run out of room. Use **Gap** for spacing instead of margins, and change the Column Class per breakpoint to reflow the whole layout with zero media queries.

## Column Class: The Most Important Sizing Tool in Divi 5

Column Class is the one to learn first. Instead of a fixed pixel width, you pick a fraction:

| Column Class | Width basis |
|---|---|
| Fullwidth | 100% |
| 3/4 | 75% |
| 2/3 | ~66% |
| 1/2 | 50% |
| 1/3 | ~33% |
| 1/4 | 25% |
| 1/6 | ~16% |
| No Column Class | Sizes to content |

Pair it with **Layout Wrapping > Wrap** and the behaviour becomes genuinely useful: columns sit side by side until they no longer fit, then wrap to the next line — each still respecting its fraction. You describe the *intent* ("this is a third") and the browser handles the arithmetic. Which is a good division of labour, because the browser is better at arithmetic than I am after 4pm.

## The Six Controls You'll Actually Use

The whole system is really six settings working together:

1. **Column Class** — width basis
2. **Layout Wrapping** — whether columns wrap
3. **Gap** — spacing between things
4. **Justify Content** — distribution along the main axis
5. **Align Items** — alignment across the cross axis
6. **Display Order** — visual reordering per breakpoint

Learn the first three properly and you'll build 90% of layouts. The other three are for when something specific isn't behaving.

## A Real Build, Step by Step

Here's a mixed-width row that reflows cleanly:

1. **Configure the Row.** In the Design tab's Layout group, set a **25px Horizontal Gap** and **25px Vertical Gap**, then enable **Layout Wrapping > Wrap**. The vertical gap matters — that's the spacing between wrapped lines.
2. **First column:** Column Class **2/3**, 15px Vertical Gap, two Text modules inside.
3. **Second column:** Column Class **1/2**, 15px Vertical Gap, with Image, Heading and Text modules plus borders.
4. **Third column:** Column Class **1/3**, 25px padding, **Justify Content: Space Between**, containing a Module Group with a 5px Vertical Gap.
5. **Fourth column:** Column Class **1/6**, with Module Groups at 0px Vertical Gap.
6. **Responsive:** on **Tablet**, change Column Classes — set the first column to Fullwidth. On **Phone**, apply the **Single Row** Structure Template rather than editing every column individually.

That last step is the time-saver nobody mentions. On phone, don't fiddle with four Column Class values — swap the Structure Template and be done.

## Gap Replaces Margins (Mostly)

This is the habit change that trips up anyone coming from Divi 4. The rule:

- **Row-level Gap** → gutters between columns, and spacing between wrapped lines
- **Column or Module Group Gap** → spacing between modules inside
- **Margin** → one-off offsets and intentional overlaps only

Why it matters: gap applies *between* items, so you never get the classic trailing-margin problem where the last card in a row has 25px of pointless space hanging off it. Margin on children creates that. Gap on the parent doesn't.

If you're migrating an older layout, this is one of the bigger differences — worth skimming [what changed between Divi 4 and Divi 5](/blog/divi-5-vs-divi-4-what-changed/) before you rebuild anything.

## Responsive Column Class: One Structure, Three Breakpoints

The headline benefit: set a different Column Class per breakpoint and one structure reflows across desktop, tablet and phone **without media queries and without duplicating content**.

A four-across feature row becomes two-across on tablet and stacked on phone by changing three values. No duplicate sections hidden per device. No `@media` blocks in the Custom CSS box that you'll forget about in four months.

Which reminds me — if you've been achieving responsive layouts by duplicating sections and hiding them, [there's a cleaner way to hide sections in Divi 5](/blog/how-to-hide-a-section-in-divi-5/), but with Column Class you often don't need to hide anything at all.

## My Take: Start Simple and Add Controls Only When Something Breaks

Here's my one strong opinion: **most broken Flexbox layouts are over-configured, not under-configured.**

I've built over 100 Divi sites and the debugging pattern is almost always the same. Someone sets Column Class, then Justify Content, then Align Items, then Grow To Fill, then Display Order, all at once — and now four settings are fighting and nobody knows which one is winning. The layout looks wrong and every fix makes it wronger.

The fix is boring: set Column Class and Gap. Look at it. *Then* add Justify Content, Align Items or Grow/Shrink only when they solve a specific, named problem. If you can't say what a setting is fixing, take it off.

And on **Display Order**: it reorders visually, not logically. The document order stays put, which means keyboard users and screen readers still get the original sequence. Use it sparingly, and actually tab through the page afterwards. Someone will, eventually — you may as well be first.

## When to Reach for CSS Grid Instead

Flexbox isn't always right. Switch to Grid when:

- Rows *and* columns must align to each other in both directions
- You need items to span multiple rows and columns in a deliberate pattern
- It's a genuine two-dimensional layout, like a magazine grid or a dashboard

The goal isn't to force every design into Flexbox. It's to use Flexbox for the 90% where it's faster, and Grid for the 10% where it's correct.

## Straight Answers

**How do you create responsive columns without CSS Grid?**
Column Class for widths, Layout Wrapping set to Wrap so they flow onto new lines.

**What is Column Class?**
A width basis set as a fraction — Fullwidth through 1/6 — instead of fixed pixels.

**Flexbox or CSS Grid?**
Flexbox for card grids, sidebars and feature rows. Grid for true two-dimensional layouts.

**Do I still need margins?**
Mostly no. Use Gap on the container. Keep margin for one-off offsets and overlaps.

**Can columns reorder on mobile?**
Yes, via Display Order per breakpoint — but test keyboard focus, because document order doesn't change.

**Do I need media queries?**
No. A different Column Class per breakpoint reflows one structure across all three.

## The Last Word

Column Class plus Wrap plus Gap. That's the trio. Everything else in [Divi 5's](https://www.elegantthemes.com/affiliates/idevaffiliate.php?id=81533) Flexbox system is a refinement on top of those three.

Start with simple fractions, resist the urge to switch on every control at once, and test with real content instead of placeholder text — because placeholder text is a professional liar and will happily hide a layout problem until launch day.

Next up in the series: [best practices and the mistakes to avoid](/blog/et-part-10-of-mastering-flexbox-best-practices-helpful-tips/). And if a layout is refusing to behave no matter which setting you poke, [I'm available](#contact) — I've poked all of them.

---

*This is a summary of [Elegant Themes' original post, "Part 9 Of Mastering Flexbox: Creating Responsive Columns Without CSS Grid"](https://www.elegantthemes.com/blog/divi-resources/part-9-of-mastering-flexbox-creating-responsive-columns-without-css-grid). All credit for the original content goes to Elegant Themes.*
