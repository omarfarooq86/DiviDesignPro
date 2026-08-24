---
title: 'Divi 5 Speed Optimization: 8 Fixes That Actually Move the Score'
description: 'Divi 5 speed optimization in the order that works — images first, hosting, Divi performance options, caching last. Plus why your Lighthouse score and Search Console disagree.'
date: 2026-05-14
updated: 2026-08-23
category: 'Divi Tips'
featuredImage: '/blog-images/divi-5-speed-optimization-tips-ai.webp'
tags:
  - 'divi 5 speed optimization'
  - 'divi core web vitals'
  - 'make divi faster'
hasFAQ: true
faqData:
  - question: 'Is Divi 5 fast enough without optimization?'
    answer: 'Divi 5 gives a much better baseline than Divi 4 because it replaced shortcode storage with structured data. It still is not automatically fast — hosting, images and caching are yours to handle.'
  - question: 'What slows down a Divi site the most?'
    answer: 'Images, by a wide margin. Oversized uncompressed hero images account for most of the weight on most Divi sites. Plugins come second and hosting third.'
  - question: 'Which Divi performance options should I enable?'
    answer: 'Dynamic Module Framework, Dynamic CSS, Dynamic Icons and Improve Google Fonts Loading are safe on nearly every site. Defer jQuery and Critical CSS are worth real gains but test them, as they break some plugins.'
  - question: 'What are good Core Web Vitals scores?'
    answer: 'LCP under 2.5 seconds, INP under 200 milliseconds and CLS under 0.1, measured at the 75th percentile of real visits. Google uses field data, not your Lighthouse number.'
  - question: 'Does a caching plugin fix a slow Divi site?'
    answer: 'It serves the same page faster, which helps, but it does not reduce the page weight. Caching a 4MB page still delivers 4MB. Fix the images and the plugin count first, then cache.'
  - question: 'Why is my Lighthouse score good but Search Console says my Core Web Vitals are poor?'
    answer: 'Lighthouse is a lab test on a simulated device. Search Console reports field data from real visitors on real phones and networks. When they disagree, the field data is the one that affects rankings.'
---

Divi 5 removed the architectural reason Divi was slow. It did not make your site fast — that still depends on your images, your host and your plugin count. Here are the eight fixes, in the order that actually works.

> **TL;DR:** Do it in this order: **images**, **plugin audit**, **hosting**, **Divi performance options**, **fonts**, **caching**, **CDN**, **measure**. Most people start at caching, which serves a bloated page faster rather than making it smaller. Targets: **LCP under 2.5s, INP under 200ms, CLS under 0.1** — measured on real visitors, not in Lighthouse.

## 1. Fix Your Images First

This is number one because it's nearly always where the weight is, and it's the step people skip because it's tedious.

**Resize before uploading.** A hero image needs to be about 1600–1920px wide. If you're uploading straight from a phone or a stock site, you're uploading 3000–6000px. That single change often cuts a megabyte.

**Convert to WebP.** Roughly 25–35% smaller than JPEG at equivalent quality, supported everywhere that matters. ShortPixel, Imagify and Squoosh all do it; so does most modern image editing software.

**Compress.** Quality 75–82 is visually indistinguishable from 100 on photographs and a fraction of the size.

**Set real dimensions.** Images without width and height cause layout shift, which is the CLS half of Core Web Vitals. Divi outputs dimensions for media library images; hand-coded `<img>` tags in Code modules are where this breaks.

**Lazy load below the fold, never above it.** Lazy loading your hero image delays the exact element Google measures for LCP.

## 2. Audit Your Plugins

Not "deactivate the ones you don't use" — **delete** them. Deactivated plugins still sit in the filesystem as an update and security obligation.

Then look at what's left with one question: what does each one load on every page? A social sharing plugin that enqueues its CSS site-wide, including on pages with no share buttons, is costing you on every request.

Divi-specific note worth making: every third-party Divi module plugin you remove is also one fewer [Divi 5 compatibility risk](/blog/what-is-divi-5-and-why-you-should-upgrade/). Several of the most common ones — post grids, advanced tabs, filterable portfolios — are now replaceable with [native Loop Builder work](/blog/divi-5-loop-builder-dynamic-content-made-easy/).

## 3. Get Off Cheap Shared Hosting

Everything above this line is your work. This line is your host's.

Server response time is the floor under every other metric. If your **TTFB** is 1.2 seconds, you cannot have a 2.5-second LCP no matter what you do to the front end. You've spent half your budget before a single byte of content moves.

What to look for:

- **PHP 8.1 or newer** — meaningfully faster than PHP 7.x on WordPress
- **Object caching** available (Redis or Memcached)
- **NVMe or SSD storage**
- **A server near your visitors**

Test your own TTFB before assuming this is the problem. Under 200ms is good, 200–500ms is acceptable, over 800ms means the host is your ceiling.

## 4. Enable Divi's Performance Options

**Divi → Theme Options → Performance.** These are free wins and most sites have them half-configured.

| Option | What it does | Safe to enable |
|---|---|---|
| **Dynamic Module Framework** | Loads only the modules a page uses | Yes |
| **Dynamic CSS** | Only outputs CSS for what's on the page | Yes |
| **Dynamic Icons** | Loads only the icon subsets in use | Yes |
| **Improve Google Fonts Loading** | Adds preconnect and swap behaviour | Yes |
| **Disable WordPress Emojis** | Removes the emoji script | Yes |
| **Defer jQuery and jQuery Migrate** | Moves jQuery out of the critical path | **Test it** |
| **Defer Additional Third Party Scripts** | Same for other scripts | **Test it** |
| **Critical CSS** | Inlines above-the-fold styles | **Test it** |

The three marked "test it" are where the real gains are and where things break. Deferring jQuery is the most common cause of a slider that stops sliding or a form that stops validating. Critical CSS occasionally produces a visible flash of unstyled content on the first paint.

Enable them one at a time, on staging, and check a page with a form, a slider and a menu on it. If something breaks, you've found which one and you can leave it off — a working site at 82 beats a broken site at 94.

## 5. Cut Your Font Loading

Fonts are the quiet cost. Each family and weight is a separate file that can block text rendering.

**Use fewer weights.** Two families and four weights total is plenty for almost any site. Loading nine weights because the design tool offered them is common and expensive.

**Self-host where you can**, which removes a third-party connection from the critical path.

**Use `font-display: swap`** so text renders in a fallback rather than staying invisible.

One Divi 5 note: [variable fonts](/blog/et-best-variable-fonts-for-web-design-now-in-divi-5/) can be a net win here. One variable font file covering the full weight range often beats four static weights — but only if you were genuinely using four. Loading a variable font to use a single weight is a downgrade.

## 6. Then Cache

Now that the page is smaller, make it repeatable.

| Cache layer | What it does |
|---|---|
| **Page cache** | Serves prebuilt HTML instead of running PHP |
| **Browser cache** | Sets expiry headers so returning visitors re-download nothing |
| **Object cache** | Redis or Memcached for repeated database queries |

WP Rocket, FlyingPress and LiteSpeed Cache all work well with Divi. Whichever you use, learn its cache-clearing order, because Divi has a cache of its own: **Divi → Theme Options → Builder → Advanced → Static CSS File Generation → Clear**, *then* the plugin, *then* the CDN.

## 7. Add a CDN

Cloudflare's free tier is genuinely good and takes twenty minutes. Static assets get served from a location near your visitor instead of from your origin server.

Be conservative with the optimisation toggles. Auto Minify and Rocket Loader can conflict with Divi's own deferral settings, and diagnosing "which of my four optimisation layers broke this" is a bad afternoon.

## 8. Measure the Right Thing

| Tool | What it tells you |
|---|---|
| **PageSpeed Insights** | Both lab score and, if you have traffic, real CrUX field data |
| **Search Console → Core Web Vitals** | Google's own field data, grouped by URL pattern |
| **GTmetrix** | Waterfall view — best for finding *what* is heavy |
| **WebPageTest** | Multi-location, filmstrip, connection throttling |

Current thresholds, at the **75th percentile** of real page views:

- **LCP** under **2.5s** — largest element painted
- **INP** under **200ms** — responsiveness to interaction
- **CLS** under **0.1** — visual stability

That 75th percentile matters. It means a quarter of your visitors can be slower than the threshold and you still pass, and it also means one slow segment — mobile users on a poor connection — can fail you while your own device feels fine.

## My Take: Nobody's Slow Divi Site Was Ever Fixed by a Caching Plugin

Here's my one strong opinion: **caching is the last step and everyone treats it as the first, which is why so many Divi sites have three optimisation plugins and a 4MB homepage.**

I've built over 100 Divi sites and audited plenty more, and the pattern almost never varies. Someone gets a poor score, installs a caching plugin, enables every toggle in it, adds a second plugin for images, and lands maybe eight points better. Then they conclude Divi is slow.

Meanwhile the homepage has a 2400px hero JPEG at 1.4MB, four "team" photos straight off a camera at 800KB each, and a background image on a section nobody scrolls to. That's roughly 5MB of images on a page whose text content would fit in 8KB.

**Caching does not make a page smaller. It makes the same page arrive sooner.** A cached 5MB page is still 5MB down someone's mobile connection. You've optimised the delivery of the problem.

The arithmetic is what convinces people. Resizing that hero to 1600px, converting to WebP and compressing at 80 typically takes it from 1.4MB to about 140KB — a 90% cut, on the single element Google measures for LCP. Do the same to the four team photos and the page drops by 4MB. That is not a plugin you can install; it's twenty minutes in an image tool or one bulk run of ShortPixel.

So my order is deliberate and I'd defend it: **images, plugins, hosting, Divi's own options, fonts, then caching.** Caching is genuinely valuable and belongs in every build — it's just the amplifier, not the fix. Amplify a lean page and you get a fast site. Amplify a bloated one and you get a bloated site with better TTFB.

The one thing I'd add for anyone chasing a number: **stop optimising for Lighthouse.** It's a lab test on a simulated mid-tier phone, useful for finding problems and not what Google ranks on. Search Console's field data is the one that counts, it lags by up to 28 days, and I've seen a 96 in Lighthouse sitting next to a failing LCP in Search Console more than once. Fix the real page for real visitors and both numbers follow.

## Straight Answers

**Is Divi 5 fast by default?**
Better baseline than Divi 4, not automatically fast. Images, hosting and plugins are still yours.

**Biggest slowdown?**
Images, by a wide margin.

**Which Divi options are safe?**
Dynamic Module Framework, Dynamic CSS, Dynamic Icons, Google Fonts loading, disable emojis. Test the defer options and Critical CSS.

**Good Core Web Vitals?**
LCP under 2.5s, INP under 200ms, CLS under 0.1, at the 75th percentile.

**Does caching fix a slow site?**
It delivers the same weight faster. Reduce the weight first.

**Lighthouse says 95, Search Console says poor. Which is right?**
Search Console. It's real visitors, and it's what Google uses.

## The Last Word

Divi 5's rewrite removed the excuse. What's left is the unglamorous part: images sized properly, a short plugin list, a host that answers in under 300ms, and Divi's own performance options actually switched on.

Do those four and caching becomes a bonus rather than a rescue. Start with the images. It's the most boring hour in web development and it beats everything else on this page.

[Divi 5](https://www.elegantthemes.com/affiliates/idevaffiliate.php?id=81533) gives you a genuinely competitive starting point now, which wasn't true two years ago. If your Core Web Vitals are failing and you'd rather someone found the actual cause than added a fourth optimisation plugin, [that's usually a one-hour job](#contact).

## Related Reading

- [Divi 5 vs Divi 4: Every Real Difference](/blog/divi-5-vs-divi-4-what-changed/) — what the architecture rewrite did and didn't fix
- [How to Hide a Section in Divi 5](/blog/how-to-hide-a-section-in-divi-5/) — including why hiding on mobile doesn't help your score
- [Divi 5 Loop Builder](/blog/divi-5-loop-builder-dynamic-content-made-easy/) — replacing plugins with native dynamic content
