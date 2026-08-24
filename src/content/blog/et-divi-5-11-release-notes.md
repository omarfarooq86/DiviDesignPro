---
title: 'Divi 5.11 Release Notes: 4 New Modules and 18 Fixes'
description: 'Divi 5.11 adds Charts, Gravity Forms, Imagely Gallery and Payment Button modules plus 18 fixes. What actually matters, what to test, and the AI Agent teaser.'
date: 2026-08-23
category: 'Divi Tips'
featuredImage: '/blog-images/divi-ai-design.jpg'
tags:
  - 'divi 5.11'
  - 'divi 5 changelog'
  - 'divi 5 new features'
hasFAQ: true
faqData:
  - question: 'What is new in Divi 5.11?'
    answer: 'Four new modules — Charts, Gravity Forms, Imagely Gallery and Payment Button — plus 18 bug fixes and improvements, mostly around the Visual Builder and flexbox stability.'
  - question: 'Should I update to Divi 5.11 right away?'
    answer: 'If you run WooCommerce 11.0 with Theme Builder Shop templates, yes — 5.11 fixes those templates not rendering on the frontend. Otherwise stage it first, like every update.'
  - question: 'Does Divi 5.11 include the Divi AI Agent?'
    answer: 'No. The release notes tease that the Divi AI Agent is coming soon, promising chat-based orchestration inside the builder, but it did not ship in 5.11.'
  - question: 'What does the new Divi Charts module do?'
    answer: 'It builds interactive charts in nine formats, managed through a new tabular data editor, so you enter data in a spreadsheet-style grid instead of hand-coding a chart library.'
  - question: 'Is Divi 5.11 a performance release?'
    answer: 'Not really. The bulk of 5.11 is new modules and builder stability. If speed is your goal, the wins are in how you build, not this version number.'
  - question: 'Does Divi 5.11 fix the Global Color crash?'
    answer: 'Yes. Circular Global Color references no longer crash the Visual Builder, and the Variable Manager now blocks you from creating them in the first place.'
---

Divi 5.11 landed as a quick follow-up to 5.10, and it's a bigger deal than the decimal suggests: four brand-new modules and 18 fixes. If you run WooCommerce, one of those fixes alone is worth the update.

This is a "fill in the gaps" release rather than a headline release. Nobody's putting Divi 5.11 on a billboard. But it quietly removes four reasons you'd previously have reached for a third-party plugin, which is the kind of update I actually like. Fewer plugins, fewer things to break at 2am.

> **TL;DR:** Divi 5.11 adds Charts, Gravity Forms, Imagely Gallery and Payment Button modules, plus 18 fixes. Update sooner rather than later if you use WooCommerce 11.0 with Theme Builder Shop templates — that was broken and now isn't. The Divi AI Agent is teased for "soon," not included here.

## What's New in Divi 5.11: Four Modules

Each of these replaces something you were probably doing with a plugin or a shortcode.

| New module | What it does | What it replaces |
|---|---|---|
| **Charts** | Interactive charts in nine formats, built via a new tabular data editor | A charting plugin, or an embedded image of a chart |
| **Gravity Forms** | Native module with Visual Builder preview and form selection | Pasting a shortcode and hoping |
| **Imagely Gallery** | Native gallery with Dynamic Assets-aware NextGEN loading | A NextGEN shortcode with no builder preview |
| **Payment Button** | PayPal and Stripe payment buttons | A full ecommerce plugin for a single button |

The **Charts** module is the one I'd play with first. Nine formats, and — this is the good bit — a tabular data editor. You type your numbers into a grid like a normal person instead of wrestling a JavaScript config object. Anyone who has ever hand-fed data into a chart library will understand why I'm this excited about a spreadsheet.

**Payment Button** deserves a mention too, because it solves a genuinely annoying problem. Sometimes a client doesn't need a store. They need one button that takes $50 for a consultation. Installing a full ecommerce stack for that is like buying a forklift to carry a sandwich.

## The Fixes That Actually Matter

Eighteen fixes is a lot to scroll past, so here are the ones with teeth:

- **Theme Builder Shop templates weren't rendering on the frontend with WooCommerce 11.0.** If that's you, stop reading and go update. This is the headline fix.
- **Visual Builder crashes from circular Global Color references are gone** — and the Variable Manager now stops you creating them at all. If you build with [Divi 5's global variables](/blog/divi-5-global-variables-complete-guide/), you may have hit this: Color A references B, B references A, builder falls over in a heap. Fixed, and now prevented.
- **Image module: "Open in Lightbox" plus "Grow to Fill" made images shrink instead of fill.** A bug so contrarian it deserves a slow clap.
- **CSS classes for the flex `align-items` property** were added to Column, Section, Row and Group modules — better flexbox control without custom CSS.
- **Link module showed the raw URL** when Link Text was left empty. Now it doesn't.
- **Text module list items weren't inheriting body text styles.** Small, but it's the kind of thing that makes a page look subtly wrong for reasons you can't name for twenty minutes.
- **Desktop breakpoint defaulted to a zoomed-in view** when widescreen was enabled.
- **The Return to Shop button came back** on emptied cart pages using Woo Notice and Cart Products modules.

Notice the theme: WooCommerce and flexbox. Those are the two areas Divi 5 has been steadily hardening, and 5.11 continues it.

## The Divi AI Agent Is Coming (But It Isn't Here Yet)

Buried at the end of the notes is the interesting part: the **Divi AI Agent** is coming soon, promising chat-based orchestration of AI agents inside the builder. Not "generate me an image." More like "restyle this section to match the header, and make the mobile version not embarrassing."

I'll believe it when I'm clicking it. But it's a clear signal about where [Divi](https://www.elegantthemes.com/affiliates/idevaffiliate.php?id=81533) is heading, and it fits the broader pattern — I wrote about [whether AI is going to kill WordPress](/blog/et-is-ai-going-to-kill-wordpress/) and the short version is no, it's moving in. This is what "moving in" looks like in a changelog.

## My Take: Update, But Stage It First

Here's my one strong opinion, and it applies to every Divi release, not just this one: **never update a client site directly, no matter how boring the release notes look.**

I've built over 100 Divi sites and the pattern is depressingly consistent. The updates that break things are never the scary ones. It's always the "18 minor fixes" release that trips over a plugin you forgot was installed. The scary releases get tested by everyone. The boring ones get trusted.

My actual process, which takes about fifteen minutes:

1. Back up the site. Full files and database, not just the database.
2. Update on staging.
3. Open the three pages the client cares about most — usually home, contact, and whichever page has the form.
4. Submit the form. Actually submit it. Check the email arrives.
5. Then push to production.

Step four catches more problems than steps one through three combined.

## Who Should Update Immediately

- **You run WooCommerce 11.0 with Theme Builder Shop templates.** Your shop pages may not be rendering. Go.
- **You hit Visual Builder crashes with Global Colors.** Fixed.
- **You want charts, Gravity Forms, or a payment button** without another plugin.

## Who Can Wait a Week

- **You're mid-launch on a client site.** Never update during a launch window. Ship first, update Monday.
- **You have a heavily customized child theme.** Test properly. You know why.
- **Your site is stable and you use none of the four new modules.** A week of patience costs you nothing.

## Straight Answers

**What is new in Divi 5.11?**
Four new modules — Charts, Gravity Forms, Imagely Gallery and Payment Button — plus 18 fixes, mostly Visual Builder and flexbox stability.

**Should I update right away?**
If you run WooCommerce 11.0 with Theme Builder Shop templates, yes. Otherwise stage it first.

**Does 5.11 include the Divi AI Agent?**
No. It's teased as coming soon, not shipped.

**What does the Charts module do?**
Interactive charts in nine formats, with a new tabular data editor for entering the data.

**Is this a performance release?**
No. It's modules and stability. For speed, see [Divi 5 speed optimization](/blog/divi-5-speed-optimization-tips/).

**Does it fix the Global Color crash?**
Yes, and the Variable Manager now prevents circular references entirely.

## The Last Word

Divi 5.11 is a housekeeping release with four genuinely useful new rooms added to the house. No fireworks, no drama, just fewer plugins and one significant WooCommerce fix.

Back it up, stage it, click the form, then ship it. And if a Divi update has ever ruined your evening, [I take those calls](#contact) — usually with a joke I've already used earlier in the post.

See you in 5.12.

---

*This is a summary of [Elegant Themes' original post, "Divi 5.11 Release Notes"](https://www.elegantthemes.com/blog/divi-resources/divi-5-11-release-notes). All credit for the original content goes to Elegant Themes.*
