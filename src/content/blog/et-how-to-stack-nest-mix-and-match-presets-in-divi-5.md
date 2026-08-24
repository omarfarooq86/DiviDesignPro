---
title: 'Divi 5 Presets: How to Stack, Nest, Mix and Match Them'
description: 'Divi 5 presets can stack and nest like a real design system. Learn how to layer presets, nest them inside each other, and change one value site-wide.'
date: 2026-08-23
category: 'Divi Tips'
featuredImage: '/blog-images/divi-ai-design.jpg'
tags:
  - 'divi 5 design presets'
  - 'divi 5 presets'
  - 'divi design system'
hasFAQ: true
faqData:
  - question: 'Can you apply more than one preset to an element in Divi 5?'
    answer: 'Yes. That is called stacking. You can apply several presets to the same element or option group, and Divi merges them into one final style.'
  - question: 'What is the difference between stacking and nesting presets in Divi 5?'
    answer: 'Stacking applies multiple presets side by side to the same element. Nesting puts presets inside other presets, so an Element Preset can contain Option Group Presets as live references.'
  - question: 'Do nested presets stay linked or get flattened?'
    answer: 'They stay linked. When you save an Element Preset, its Option Group Presets remain live references, not flattened copies, so edits still flow through every layer.'
  - question: 'What is the difference between an Option Group Preset and an Element Preset?'
    answer: 'An Option Group Preset saves one group of settings, such as border or background. An Element Preset saves a whole module, and can contain Option Group Presets inside it.'
  - question: 'Should presets use Design Variables?'
    answer: 'Yes. Store raw colors, spacing and fonts in the Variable Manager first, then build presets that reference those variables instead of hardcoded values.'
  - question: 'How many presets should one element have?'
    answer: 'Keep each preset small with one job. Four focused presets on a module — base, spacing, surface, variant — is normal and far easier to maintain than one giant preset.'
---

Yes, you can apply more than one preset to the same element in Divi 5. That single fact turns presets from a shortcut into an actual design system, and most people have no idea it's possible.

Here's the mindset shift: stop saving finished designs as presets. Start saving *pieces*. Make each preset small, give it one job, and let Divi combine them. Change a shared piece once and every connected element on the site updates. It's less like saving outfits and more like owning trousers.

> **TL;DR:** Divi 5 presets do two clever things. **Stacking** applies several presets to one element at once. **Nesting** puts presets inside other presets as live references — so editing a nested border preset updates every button that uses it, everywhere. Build small, single-purpose presets on top of Design Variables and the whole site becomes editable from one place.

## Stacking Presets: Layer Them Like CSS Classes

Stacking means applying more than one preset to the same element or option group. Divi merges them into one final style.

The pattern I use on every build is four layers:

| Layer | Job | Example |
|---|---|---|
| **Base** | Typography and core look | Body font, size, color |
| **Spacing** | Padding and margin rhythm | 25px inner padding |
| **Surface** | Background and border | White card, 1px border, radius |
| **Variant** | The one thing that differs | Dark mode, accent color |

A single Blurb module can carry all four at once. Now here's why that matters: when the client says "can all the cards have slightly more breathing room" — and they will say that, roughly one hour after approving the design — you edit the spacing preset. Once. Every card on the site moves.

Compare that to the old way, where "card" was one giant preset and you'd saved six near-identical variations of it. Changing padding meant editing all six and missing one. There's always one. It's usually on the page the client checks first.

## Nesting Presets: Presets Inside Presets

Nesting is the part that sounds impossible until you see it. Presets can live *inside* other presets.

When you save an Element Preset, its Option Group Presets stay embedded as **live references**, not flattened copies. So you can build a chain:

- A **"Border 100%"** Option Group Preset
- nested inside a **"Button Global"** preset
- nested inside a **"CTA – Global"** Element Preset

Change the border radius in "Border 100%" and it travels up through "Button Global," through "CTA – Global," and out to every CTA section on the site. One edit, three layers deep, site-wide.

This is genuinely the same idea as [Divi 5's global variables](/blog/divi-5-global-variables-complete-guide/), just applied to groups of settings instead of single values. Variables handle "what colour is our blue." Presets handle "what does a button look like." Together they're a design system that a normal human can maintain.

## Mixing vs Matching: Two Different Moves

These sound like the same word twice. They're not.

**Mixing** creates variations by swapping only the layer that changes. A light card and a dark card share the base, spacing and border presets, and differ only in the surface preset. One difference, not two whole designs.

**Matching** reuses one preset anywhere a compatible option group exists. Your "Border 100%" preset works on a button, a footer, a testimonial, and a row. Same preset, four module types. This is the one people under-use — they build presets per module type when the preset doesn't care what module it's on.

## How to Build It: Five Steps

1. **Start with Design Variables.** Open the Variable Manager and store your raw values — colors, spacing, font sizes. Presets should reference these, never hardcode them. This is the foundation; skip it and you're building on sand.
2. **Create small Option Group Presets.** Border, background, spacing — one job each. Save via the Preset icon in the option group.
3. **Nest them into a component preset.** Build a "Button Global" preset that contains your border and spacing presets as live references.
4. **Save the full module as an Element Preset.** Your "CTA – Global" preset now carries all the nested pieces in one click.
5. **Mix and match across the site.** Swap one layer for light/dark variants. Reuse compatible presets across module types.

If you're coming from Divi 4, this is one of the bigger mental shifts — worth reading [what actually changed in Divi 5](/blog/divi-5-vs-divi-4-what-changed/) if the Variable Manager is new to you.

## My Take: The Real Win Isn't Speed, It's Handover

Here's my one strong opinion: **presets aren't a time-saver, they're a liability-saver.**

Everyone sells presets on build speed. Fine, they help. But I've built over 100 Divi sites and the thing that actually costs money isn't the build — it's month seven, when the client emails "can we make the buttons a bit rounder" and you open a site you last touched in March.

On a site built with stacked and nested presets, that email is a two-minute job. On a site built with fifty one-off module styles, it's an afternoon of hunting, and you'll still miss the button in the footer. You always miss the button in the footer.

So the honest pitch is this: build with presets so that *future you*, or whoever inherits the site, can make a global change without opening forty pages. That's the whole game. If you're handing a site to a client team, this is the difference between "they can maintain it" and "they'll call you every time."

## Common Mistakes

- **Building one giant preset per module.** That's Divi 4 thinking. Break it into layers.
- **Hardcoding values instead of using variables.** Works today, painful in six months.
- **Making presets so granular you can't remember them.** There's a middle ground. Four layers, not fourteen.
- **Naming presets after where they're used, not what they do.** "Homepage Card" ages badly. "Card – Surface" doesn't.

## Straight Answers

**Can you apply more than one preset to an element?**
Yes. Stacking lets you apply several presets to the same element or option group, and Divi merges them.

**What's the difference between stacking and nesting?**
Stacking applies presets side by side. Nesting puts presets inside other presets.

**Do nested presets stay linked?**
Yes — they remain live references, not flattened copies, so edits flow through every layer.

**Option Group Preset vs Element Preset?**
Option Group saves one group of settings. Element saves a whole module, and can contain Option Group Presets.

**Should presets use Design Variables?**
Yes. Store raw values in the Variable Manager, then reference them from presets.

**How many presets per element?**
Keep each small and single-purpose. Four focused presets is normal and easier to maintain than one big one.

## The Last Word

Stacking and nesting turn Divi 5 presets from a copy-paste convenience into something that behaves like a proper design system. Small pieces, connected, edited once.

Build it this way and changing the whole site's button radius takes one click. Build it the other way and it takes an afternoon and a small amount of your will to live.

If you'd rather someone else set up the design system and hand you something maintainable, [that's what I do](#contact) — and I'll name the presets properly, which is more than I can say for my own project folders.

---

*This is a summary of [Elegant Themes' original post, "How To Stack, Nest, Mix, And Match Presets In Divi 5"](https://www.elegantthemes.com/blog/divi-resources/how-to-stack-nest-mix-and-match-presets-in-divi-5). All credit for the original content goes to Elegant Themes.*
