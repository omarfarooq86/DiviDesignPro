---
title: 'Divi 5 Gradient Variables: Define Once, Use Site-Wide'
description: 'Divi 5 gradient variables turn gradients into reusable design tokens. Create linear, circular, elliptical and conical gradients in the Variable Manager and edit them once.'
date: 2026-07-30
updated: 2026-08-23
category: 'Divi Tips'
featuredImage: '/blog-images/the-beauty-of-divi-5s-gradient-variables.webp'
tags:
  - 'divi 5 gradient variables'
  - 'divi 5 global variables'
  - 'divi design system'
hasFAQ: true
faqData:
  - question: 'How do you create a gradient variable in Divi 5?'
    answer: 'Open the Variable Manager from the left toolbar, choose the Gradients category, and click Add Global Gradient. Set the type, add color stops, set direction, then name and save it.'
  - question: 'What gradient types does Divi 5 support?'
    answer: 'Four: Linear, Circular, Elliptical and Conical. Linear and Conical get an angle control for direction. Circular and Elliptical get a position control for their origin.'
  - question: 'Can you convert an existing gradient into a variable?'
    answer: 'Yes. Right-click the gradient field on any element and choose Convert to Variable. It produces the same named variable as building one from scratch.'
  - question: 'What is the difference between pasting a gradient and using a variable?'
    answer: 'A pasted gradient is an independent copy, so ten pastes means ten separate gradients. A variable keeps every element pointed at one source, so editing it updates all of them.'
  - question: 'Can you apply a gradient to text in Divi 5?'
    answer: 'Yes. In a text option group, set Fill Type from None to Gradient, then pick a variable in the Gradient Fill control that appears below.'
  - question: 'How many gradients should a site use?'
    answer: 'Few. Three intentional gradients usually look stronger than fifteen unrelated ones, and gradient text works best on large display type rather than body copy.'
---

Divi 5 gradient variables let you define a gradient once and point every element at it. Change the variable, and every section, button and heading using it updates at the same time.

Here's the distinction that makes this worth your afternoon: **if you paste the same gradient into ten places, you now have ten separate gradients.** A variable keeps all ten pointed at one source. Same visual result on day one, wildly different on day ninety when the brand colour shifts.

> **TL;DR:** Open the **Variable Manager** → **Gradients** → **Add Global Gradient**. Pick one of four types (Linear, Circular, Elliptical, Conical), set your stops, name it by role, and save. Then apply it in any Background option group's Gradient tab, on buttons, or as a text Fill Type. Build the stops from existing colour variables and keep the total list under about five.

## Divi 5's Four-Layer Design Chain

Gradient variables aren't a standalone feature — they're one rung on a ladder:

| Layer | What it holds |
|---|---|
| **Design Variables** | Raw reusable values — colors, fonts, numbers, images, links, text, gradients |
| **Option Group Presets** | Reusable styles per group — Background, Text, Border, Box Shadow, Spacing |
| **Element Presets** | A complete design for one element type |
| **Pages and Templates** | Where it all lands |

One useful asymmetry: **Option Group Presets are cross-element** — a Background preset works on a Section, Row, Column, Group, Blurb or Call To Action. **Element Presets are type-locked** — a Button preset only touches Button modules.

The nesting flow worth copying: colour variables (**Brand Primary**, **Brand Secondary**) become the stops in a gradient variable, which feeds a Background Option Group Preset, which gets deployed across the site. Change Brand Primary and the change travels the whole chain.

## How to Create a Gradient Variable

**Method 1 — from the Variable Manager:**

1. Open the **Variable Manager** from the left toolbar.
2. Choose the **Gradients** category.
3. Click **Add Global Gradient**. The gradient picker opens.
4. Pick a type: **Linear**, **Circular**, **Elliptical** or **Conical**.
5. Add colour stops, set each stop's colour, and drag stops along the bar to position them.
6. Set direction — Linear and Conical use an **angle control**; Circular and Elliptical use a **position control** for the origin (center, top left, bottom right).
7. Name it and save.

**Method 2 — convert what you already built:** right-click the gradient field on any element and pick **Convert to Variable**. Same result, less clicking. This is the one to use when you're retrofitting an existing site.

## Where You Can Apply Them

**Backgrounds** — element settings → **Background** option group → **Gradient** tab → click the gradient field → pick the variable. Works on Sections, Rows, Columns, Groups and Modules.

**Buttons** — open a Button module → **Background** → **Gradient** tab → choose the variable. Then save it as a Button Element Preset so you're not repeating yourself.

**Text fills** — inside a **Text**, **Heading Text** or **Title Text** option group (availability varies by module), set **Fill Type** from None to **Gradient**. A **Gradient Fill** control appears below; pick your variable there. You can add a text stroke too, and fill and stroke work independently — gradient fill alone, fill plus stroke, or a transparent fill showing only the stroke.

One scope caveat: variables work anywhere Divi exposes a compatible gradient control. Not every field everywhere.

## Name Them by Role, Not by Colour

This is the habit that ages well. "Blue to Purple" tells you nothing in six months and becomes a lie the moment the brand changes. Role-based names survive rebrands:

**Brand Gradient**, **Hero Glow**, **Accent Wash**, **CTA Gradient**, **Heading Gradient**.

For a typical background set: **Hero Background**, **Soft Section Wash**, **Dark CTA Gradient**, **Footer Accent**. Four names, four jobs, no colours mentioned.

This is exactly the same principle as [naming colour variables properly](/blog/divi-5-global-variables-complete-guide/), and the reason both matter is identical: the name is documentation for whoever opens the site next, including you.

## My Take: Three Gradients, Not Fifteen

Here's my one strong opinion: **the sites that look most expensive use the fewest gradients.**

Elegant Themes puts it well — a site with three intentional gradients usually feels stronger than one with fifteen unrelated ones. I'd go further. I've built over 100 Divi sites and every single time I've inherited a site that felt visually noisy, the cause was gradient sprawl: a hero gradient, a different section gradient, a third on the buttons, a fourth on a card, none of them related, all of them individually fine.

Variables make this problem *easier* to create, because now adding a gradient costs almost nothing. That's the trap. Before variables, a fifteenth gradient meant fifteen minutes of fiddling and you'd talk yourself out of it. Now it's a click.

So set a hard limit before you start. Three variables. One for the hero, one for section washes, one for CTAs. If a design "needs" a fourth, look hard at whether it actually needs one of the existing three used differently.

And on gradient text specifically: keep it on **large display type** — hero headings, editorial titles, pricing headlines, campaign wordmarks. On body copy the colour stops compress into small letterforms and legibility drops fast. Also check contrast at both ends; a stop that runs too light is an accessibility problem wearing a nice outfit.

## Pair Variables With Presets

The division of labour: the **variable stores** the gradient, the **preset distributes** it.

Build a Background Option Group Preset that references your gradient variable, then apply that preset across sections. Now you have two levels of control — change the gradient variable to alter the colours, or change the preset to alter how the gradient is applied. [Stacking and nesting presets](/blog/et-how-to-stack-nest-mix-and-match-presets-in-divi-5/) is where this stops being a convenience and starts being a design system.

If gradients are new to you, the same logic applies to [reusable border and shadow presets](/blog/et-how-to-create-reusable-border-and-shadow-presets-in-divi-5/) — different option group, identical thinking.

## Straight Answers

**How do you create a gradient variable?**
Variable Manager → Gradients → Add Global Gradient. Set type, stops, direction, name, save.

**What gradient types are supported?**
Linear, Circular, Elliptical and Conical. Linear and Conical use an angle; Circular and Elliptical use a position.

**Can you convert an existing gradient?**
Yes — right-click the gradient field and choose Convert to Variable.

**Pasting vs using a variable?**
Ten pastes give you ten independent gradients. A variable keeps all ten linked to one source.

**Can you apply a gradient to text?**
Yes — set Fill Type to Gradient in a text option group, then pick a variable in Gradient Fill.

**How many gradients should a site use?**
Three intentional ones beat fifteen unrelated ones. Keep gradient text on large display type.

## The Last Word

Gradient variables are a small feature with a large downstream effect. Build them from colour variables, name them by role, apply them through presets, and a rebrand becomes a five-minute job in the Variable Manager instead of a week of hunting.

Three gradients. Role-based names. Large type only. That's the whole discipline, and [Divi 5](https://www.elegantthemes.com/affiliates/idevaffiliate.php?id=81533) makes the rest mechanical.

If your site has accumulated a gradient for every occasion and you'd like someone to consolidate them without breaking anything, [that's a job I enjoy more than I should](#contact).

---

*This is a summary of [Elegant Themes' original post, "The Beauty Of Divi 5's Gradient Variables"](https://www.elegantthemes.com/blog/divi-resources/the-beauty-of-divi-5s-gradient-variables). All credit for the original content goes to Elegant Themes.*
