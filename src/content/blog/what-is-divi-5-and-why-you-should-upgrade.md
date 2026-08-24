---
title: 'What Is Divi 5? Features, Upgrade Path and Real Risks (2026)'
description: 'Divi 5 explained: the architecture rewrite, Design Variables, presets, Loop Builder, Flexbox and CSS Grid — plus the one thing to audit before you upgrade from Divi 4.'
date: 2026-05-14
updated: 2026-08-23
category: 'Divi Tips'
featuredImage: '/blog-images/what-is-divi-5-and-why-you-should-upgrade-ai.webp'
tags:
  - 'what is divi 5'
  - 'divi 5 upgrade'
  - 'divi 4 to divi 5'
hasFAQ: true
faqData:
  - question: 'What is Divi 5?'
    answer: 'A complete rebuild of the Divi platform. Divi 4 stored layouts as WordPress shortcodes; Divi 5 uses structured data, which is what makes the faster builder, cleaner front-end output and features like Design Variables possible.'
  - question: 'Is upgrading from Divi 4 to Divi 5 safe?'
    answer: 'For most sites, yes — layouts convert and content carries over. The real risk is not Divi itself but third-party Divi module plugins and custom child themes, which need Divi 5 compatible versions.'
  - question: 'What are the main new features in Divi 5?'
    answer: 'Design Variables, option group and element presets, the Loop Builder, a visual CSS Grid editor, full Flexbox controls, Workspaces with a Command Center, Aspect Ratio and image framing, text fill options and variable font axes.'
  - question: 'Will my Divi 4 layouts still work in Divi 5?'
    answer: 'Yes. Existing layouts and content are converted and carry over. What may not carry over is anything depending on a third-party module plugin or custom builder code written against the Divi 4 API.'
  - question: 'Is Divi 5 faster than Divi 4?'
    answer: 'Yes, both in the builder and on the front end. The architecture rewrite was largely about removing the shortcode overhead that made Divi 4 heavy, which was its most-cited weakness for a decade.'
  - question: 'How much does Divi 5 cost?'
    answer: 'Around 89 dollars a year or 249 dollars for a lifetime licence, both covering unlimited sites. Existing Divi customers get Divi 5 as part of their active licence at no extra cost.'
---

Divi 5 is not a feature release. It's a rebuild of the thing underneath — and understanding that one change explains every other item on the list.

> **TL;DR:** Divi 4 stored layouts as **shortcodes**. Divi 5 stores them as **structured data**. That rewrite is what makes the faster builder, the cleaner front-end output, **Design Variables**, **presets**, the **Loop Builder**, **CSS Grid** and **Flexbox** controls possible. Existing licences include it. Before upgrading, audit your **third-party Divi plugins and child theme** — that's the only real risk.

## The Change That Matters

Divi 4 wrapped every module in a WordPress shortcode. It worked, and it carried a permanent tax: the front end had to parse and expand all of it on every page load, and the builder had to keep a shortcode string in sync with what you saw on screen.

Divi 5 stores layouts as **structured data** instead. The builder reads and writes it directly, the front end renders without the shortcode round-trip, and the output is dramatically leaner.

Two consequences follow, and they're the real reason to care:

**The bloat criticism is largely answered.** That was the standard objection to Divi for a decade, and it was fair. Divi 5 addresses it architecturally rather than by removing features.

**New features became possible.** You cannot build a global variable system on top of shortcodes without it being a hack. Structured data is what makes variables, presets and the Loop Builder work properly rather than approximately.

## What You Actually Get

### Design Variables

Colours, fonts, spacing values, numbers and gradients defined once in the **Variable Manager** and referenced everywhere. Change the variable, every element using it updates.

This is the feature that changes how you work rather than what you can make. A site built on variables can be rebranded in twenty minutes. A site built with hex codes typed into modules takes a day and you'll still miss three. Full detail in [the Divi 5 global variables guide](/blog/divi-5-global-variables-complete-guide/).

### Presets

Two kinds, and the distinction matters. **Element presets** style a whole module. **Option group presets** style one group of settings — just the border, just the box shadow, just the typography — so you can mix them. Managed in the **Preset Manager**.

### Loop Builder

Dynamic content without code. Design one card, set a **Query Type**, and Divi generates every instance — blog posts filtered by category, team members from a custom post type, WooCommerce products, even menu items. This is what turns Divi from a page builder into a site builder, covered properly in [the Loop Builder guide](/blog/divi-5-loop-builder-dynamic-content-made-easy/).

### CSS Grid and Flexbox

A **visual CSS Grid editor** — drag to resize grid items, set offsets, span columns. And real **Flexbox controls** on rows, columns and groups: Gap, Justify Content, Align Items, Layout Wrapping and Display Order.

Display Order is the quiet one. It reorders elements per breakpoint, so a CTA that sits third on desktop can be first on mobile without duplicating modules. [Divi 5's responsive column controls](/blog/et-part-9-of-mastering-flexbox-creating-responsive-columns-with/) go through the practical patterns.

### Workspaces and the Command Center

Save your builder layout — which panels are open, where they're docked, twenty-odd preferences — and recall it in one click. **Cmd+K** or **Ctrl+K** opens a Command Center for switching workspaces, saving, updating and resetting. The [complete Workspaces reference](/blog/et-everything-you-need-to-know-about-workspaces-in-divi-5/) has every setting.

### Image Framing

**Aspect Ratio**, **Object Fit** and **Object Position** as native settings. One ratio across a blog grid and every card matches regardless of what your client uploaded. This solved more real layout problems for me than any other Divi 5 addition.

### Typography

**Text Fill** — None, Gradient, Image or Transparent — plus stroke width and colour, so gradient headings and image-masked type stop being a Photoshop job. And **variable font axes** exposed in the Design tab through the updated Google Fonts integration, including intermediate weights that static fonts never offered.

### Performance

Faster builder, faster page render, better Core Web Vitals out of the box. Not the lightest builder on the market, but no longer the heavy one. If you're chasing scores, [the Divi 5 speed checklist](/blog/divi-5-speed-optimization-tips/) covers what still needs doing manually.

## Who Benefits Most

| User | What changes for them |
|---|---|
| **Site owners** | Faster site, easier edits, better Core Web Vitals |
| **Freelancers** | Variables and presets cut build time and rework |
| **Agencies** | Brand consistency across client sites, unlimited-site licence |
| **Developers** | Structured data instead of shortcode parsing |
| **Content teams** | Loop Builder means archives that maintain themselves |

## The Upgrade Process

1. **Back up.** Files and database. Non-negotiable.
2. **Stage it.** Clone to a staging site and upgrade there first.
3. **Audit third-party plugins** — see below. This is the step people skip.
4. **Update Divi** from the WordPress dashboard.
5. **Open your key pages** in the builder and check they render.
6. **Check the front end** at desktop, tablet and phone.
7. **Enable Divi 5's performance options** in Theme Options.
8. **Clear caches** — Divi static CSS first, then page cache, then CDN.

Layouts and content carry over. The conversion is designed to be backward compatible and generally is.

If you want the itemised before-and-after, [Divi 5 vs Divi 4](/blog/divi-5-vs-divi-4-what-changed/) is the side-by-side, and [the ten questions everyone asks](/blog/divi-5-the-10-questions-every-user-is-asking-right-now/) covers the specific upgrade worries.

## My Take: Divi Isn't the Risk — Your Plugin Stack Is

Here's my one strong opinion: **the only thing worth auditing before a Divi 5 upgrade is your third-party plugins and child theme, and almost nobody does it.**

I've built over 100 Divi sites and I've been called in on a number of upgrades that went wrong. In every single case the cause was the same, and it was never Divi core. It was a **third-party Divi module plugin** — one of the addon packs that adds forty extra modules — or a **child theme with custom builder code written against the Divi 4 API**.

The mechanism is straightforward once you see it. Those plugins register modules through Divi's builder API. Divi 5 rewrote that API, because it rewrote everything. Until the plugin author ships a Divi 5 compatible version, their modules are running against an interface that no longer exists. What you get isn't a clean error — it's a section that renders blank on the front end while looking fine in the builder, which is the worst kind of failure because you'll find it a week later.

So the audit, and it takes fifteen minutes:

1. List every active plugin with "Divi" in the name.
2. Check each one's changelog for explicit Divi 5 support.
3. Note every page that uses one of their modules.
4. If a plugin has no Divi 5 release, **you are not upgrading yet** — you're waiting, or replacing those modules with native ones first.
5. If you have a child theme with custom functions hooking Divi, have someone read it.

A stock Divi 4 site with no addon plugins upgrades cleanly nearly every time. A site with six addon packs and a bespoke child theme is a project, not an update.

The corollary I'd underline: **don't do this on a live site on a Friday.** Not because Divi 5 is fragile, but because the failure mode is delayed and silent, and you want to be at your desk when someone spots it.

## Any Reason to Stay on Divi 4?

Three, and only three:

**A third-party plugin you depend on has no Divi 5 version.** Legitimate. Wait for it or replace it.

**A mission-critical site in a revenue-critical window.** Don't upgrade during your busiest fortnight. Do it in a quiet week with a rollback plan.

**A heavily customised child theme nobody has read in two years.** Get it audited first.

Outside of those, there's no case for new projects. Divi 5 is where the development is going, and Divi 4 sites are accumulating a migration you'll do eventually anyway. Starting a new build on Divi 4 in 2026 means choosing to do that work twice.

## Straight Answers

**What is Divi 5?**
A full rebuild. Shortcodes replaced by structured data, which enabled everything else.

**Is upgrading safe?**
Usually. The risk is third-party module plugins and custom child themes, not Divi.

**Main new features?**
Design Variables, presets, Loop Builder, CSS Grid, Flexbox, Workspaces, Aspect Ratio, text fill, variable fonts.

**Will Divi 4 layouts work?**
Yes, they convert. Third-party modules may not.

**Is it faster?**
Yes, builder and front end both.

**Cost?**
~$89/year or ~$249 lifetime, unlimited sites. Included with an active licence.

## The Last Word

Divi 5's headline is a rebuilt architecture, and the reason to care is what the rebuild allowed: variables that make a site restylable, presets that keep it consistent, and a Loop Builder that makes archives maintain themselves.

The upgrade is genuinely low risk for a stock site. Audit your addon plugins first anyway — fifteen minutes there saves the week where a section renders blank and nobody knows why.

[Divi 5](https://www.elegantthemes.com/affiliates/idevaffiliate.php?id=81533) is included with any active licence, so for most people this is a decision about timing rather than money. If you'd like the plugin audit run before you touch a live site, [that's an hour well spent](#contact).

## Related Reading

- [Divi 5 vs Divi 4: What Changed](/blog/divi-5-vs-divi-4-what-changed/) — the itemised comparison
- [Divi 5: The 10 Questions Everyone Is Asking](/blog/divi-5-the-10-questions-every-user-is-asking-right-now/) — quick answers to upgrade worries
- [Divi 5 Global Variables: Complete Guide](/blog/divi-5-global-variables-complete-guide/) — the feature that changes how you build
