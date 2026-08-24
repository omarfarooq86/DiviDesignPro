---
title: 'How to Hide a Section in Divi 5: 5 Methods (And Which to Use)'
description: 'Five ways to hide a section in Divi 5 — Disable, device visibility, Display Conditions, custom CSS and the Divi Library. Plus why hiding on mobile is not a speed fix.'
date: 2026-06-12
updated: 2026-08-23
category: 'Divi Tips'
featuredImage: '/blog-images/how-to-hide-a-section-in-divi-5-ai.webp'
tags:
  - 'hide a section in divi'
  - 'divi 5 visibility settings'
  - 'divi display conditions'
hasFAQ: true
faqData:
  - question: 'How do you hide a section in Divi 5?'
    answer: 'Right-click the section and choose Disable, or open its settings, go to the Advanced tab and use the Visibility options. The section stays visible in the builder and disappears from the front end.'
  - question: 'How do I hide a section on mobile only in Divi?'
    answer: 'Open the section settings, go to Advanced, then Visibility, and tick Phone under Disable On. Desktop and tablet keep showing it. Note that this hides with CSS, so the content still loads.'
  - question: 'Does hiding a section on mobile make the page faster?'
    answer: 'No, usually the opposite. Device visibility hides the section with CSS but the markup still ships and the browser still downloads its images, so mobile visitors pay the weight without seeing the content.'
  - question: 'How do I schedule a section to appear on a specific date in Divi?'
    answer: 'Use Display Conditions in the Advanced tab rather than toggling visibility by hand. Divi can show or hide a section by date and time, login status, post category, author, browser and more.'
  - question: 'Is a hidden Divi section still in the HTML?'
    answer: 'It depends on the method. Fully disabling a section removes it from the front-end output. Device visibility and custom CSS leave the markup in the page and only hide it visually.'
  - question: 'Why is my hidden Divi section still showing?'
    answer: 'Almost always caching. Clear Divi static CSS first, then your page cache, then your CDN, then hard refresh. If it persists, check for a custom CSS rule overriding the visibility setting.'
---

You want a section gone from the live site but not gone from your work. Divi 5 gives you five ways to do that, and they behave very differently — one removes the markup entirely, three leave it in the page, and only one can hide a section on a schedule.

> **TL;DR:** **Disable** removes the section from front-end output entirely — use it for drafts and approvals. **Device visibility** hides with CSS, so the content still loads. **Display Conditions** is the right tool for seasonal and scheduled content, and it's the method most guides skip. **Custom CSS** for JavaScript-driven cases. **Save to Library, then delete** for long-term storage.

## Why Hide Instead of Delete

Deleting is fine when you're certain. You rarely are.

- A client says remove the testimonials section, then asks for it back in week three
- A seasonal promo runs for six weeks a year and needs to survive the other forty-six
- You're testing a shorter homepage and want the original one keystroke away
- Content is written and designed but the launch date is three weeks out

All four are hiding problems. Only one of them is the same hiding problem, which is why there are five methods.

## Method 1: Disable the Section

**The default answer, and the only one that removes the markup.**

Right-click the section and choose **Disable**. Or open the section settings, go to the **Advanced** tab, and use the **Visibility** options.

The section stays fully visible and editable in the Visual Builder, marked as disabled, and disappears from the front end. Content, styling and settings are all preserved.

Use it for: client approval workflows, half-finished sections, anything you want out of the live page right now.

## Method 2: Hide on Specific Devices

Section settings → **Advanced** → **Visibility** → **Disable On**, then tick **Phone**, **Tablet** or **Desktop**.

A tall hero that works at 1440px can be a scrolling chore at 390px. A dense comparison table can be genuinely unreadable on a phone. Both are legitimate reasons to hide per device.

What this is *not* is a performance fix. See the opinion section, because this is the single most misunderstood setting in Divi.

## Method 3: Display Conditions

**This is the method most tutorials on this topic leave out, and it's the correct answer for at least half of the reasons people hide sections.**

Section settings → **Advanced** → **Conditions**. Instead of a manual on/off toggle, you set a rule and Divi evaluates it per visitor:

| Condition type | What it does |
|---|---|
| **Date and time** | Show a promo from 24 December to 2 January, automatically |
| **Login status** | Different section for logged-in members and visitors |
| **Post or page** | Show only on specific pages, categories, tags or post types |
| **Author** | Different author bio blocks in one template |
| **Browser and OS** | Platform-specific download buttons |
| **Number of views** | Show a CTA only after someone's third visit |

If your reason for hiding is "this comes back at Christmas," a date condition beats a diary reminder. You set it once, in 2026, and it keeps working in 2029 when you've long forgotten the page exists.

Conditions also compose with Theme Builder templates, which is where they get genuinely powerful — one single-post template with three conditional author sections replaces three templates.

## Method 4: Custom CSS

For cases driven by JavaScript or a third-party tool. Add a class in **Advanced** → **CSS ID & Classes**:

```css
.hidden-section {
  display: none;
}
```

The section stays in the DOM and gets hidden visually, so your script can reveal it later by removing the class.

Two honest warnings. First, this is the wrong tool for content that should simply be absent — the markup ships either way. Second, if you're using it for A/B testing, you're serving both variants to every visitor and paying for both. Use a real testing tool for that.

## Method 5: Save to the Divi Library, Then Delete

For long-term storage, save the section to the **Divi Library** and remove it from the page.

The page stays clean, the asset is reusable across projects, and reinsertion takes one click. This is the right choice for last year's redesign, an old campaign, or a layout you might want on a different site.

One caveat carried over from Divi 4: save it as a regular Library item, not a **Global** one, unless you genuinely want every future instance to share the same content. [Divi 5 changed which tool you should reach for here](/blog/divi-5-vs-divi-4-what-changed/) — presets carry styling, the Library carries content.

## Which Method for Which Job

| Scenario | Method |
|---|---|
| Waiting on client approval | Disable |
| Half-built section, live page | Disable |
| Seasonal promo, fixed dates | **Display Conditions** |
| Members-only content block | **Display Conditions** — login status |
| Table that's unreadable on phones | Device visibility |
| Last year's redesign | Library, then delete |
| Toggled by your own JavaScript | Custom CSS |
| Genuine A/B test | None of these — use a testing tool |

## My Take: Hiding a Section on Mobile Is Not a Speed Optimisation

Here's my one strong opinion: **"hide it on mobile to make the page faster" is the most common performance mistake I find in Divi sites, and it makes mobile slower, not faster.**

Device visibility works by hiding with CSS. The section's markup is still in the HTML document. The images inside it are still referenced, so the browser still requests them. Your phone visitor downloads a 400KB hero image, three icon images and a background, then applies a rule that sets the container to `display: none`.

They paid for all of it. They saw none of it. You can confirm this yourself in about thirty seconds — view source on a page with a mobile-hidden section and search for its class, or open the network tab on a phone-sized viewport and watch the images load anyway.

I've built over 100 Divi sites, and I've been handed pages where someone hid four sections on mobile, was pleased with the tidier layout, and could not understand why the mobile Lighthouse score hadn't moved. It hadn't moved because nothing was removed. The page got visually shorter and byte-for-byte identical.

What to do instead, in order of preference:

1. **Rebuild the section to work at 390px** rather than hiding it. Usually this is a Flexbox change and a smaller heading, not a redesign — [the Flexbox best-practices post](/blog/et-part-10-of-mastering-flexbox-best-practices-helpful-tips/) covers the patterns.
2. **Disable it outright** if mobile visitors genuinely don't need it. This removes it from output, which is the thing you were trying to achieve.
3. **Fix the images.** A hero that's 400KB is the actual problem; hiding it on one breakpoint just relocates the symptom. [The Divi 5 speed checklist](/blog/divi-5-speed-optimization-tips/) has the ordering that works.

Use device visibility for what it's good at — readability and layout, where the goal is *"this doesn't work at this size."* Don't reach for it when the goal is *"this shouldn't load."* Those are different problems and Divi has a different setting for each.

## Troubleshooting

**Section still appears after hiding.** Caching, nearly every time. Clear in order: Divi → Theme Options → Builder → Advanced → **Static CSS File Generation → Clear**, then your caching plugin, then your CDN, then hard refresh. Only after all four should you go looking for a CSS conflict.

**Section vanished from the builder too.** Disabled sections stay visible in the Visual Builder with a disabled marker. If it's genuinely gone, check the page revision history — Divi writes a revision on each save.

**Hidden on desktop but showing on tablet.** Divi's breakpoints don't always match where your layout actually breaks. Check the section at the exact width where it reappears; the culprit is usually the tablet range rather than the setting.

**Display Condition not firing.** Date conditions use your WordPress site timezone, not the visitor's. Check **Settings → General** in WordPress before assuming the condition is broken.

## Straight Answers

**Fastest way to hide a section?**
Right-click, Disable. It removes the section from front-end output entirely.

**Hide on mobile only?**
Advanced → Visibility → Disable On → Phone.

**Does that make mobile faster?**
No. The markup ships and the images still download.

**Schedule a section by date?**
Advanced → Conditions → date and time. Set once, works every year.

**Is a hidden section still in the HTML?**
Disable removes it. Device visibility and custom CSS don't.

**Still showing after hiding?**
Clear Divi static CSS, then page cache, then CDN, then hard refresh.

## The Last Word

Five methods, and the choice comes down to one question: **should this content be absent, or just invisible?**

Absent means Disable, or Library-and-delete. Invisible means device visibility or CSS. And if the answer is "absent, but only on certain days or for certain people," that's Display Conditions — the setting worth learning today, because it turns a recurring manual chore into something you configure once.

[Divi 5](https://www.elegantthemes.com/affiliates/idevaffiliate.php?id=81533) includes all five, no addon required. If you've got a site where sections are hidden on mobile and the speed score won't budge, [that's usually a quick diagnosis](#contact).

## Related Reading

- [Divi Sticky Sidebar Not Working? The Real Fix](/blog/sticky-sidebar-not-working-in-divi-fix/) — another layout problem where the popular fix isn't the actual fix
- [Divi 5 Loop Builder: Dynamic Content Made Easy](/blog/divi-5-loop-builder-dynamic-content-made-easy/) — build sections that adapt instead of hiding them by hand
- [Divi 5 Speed Optimization Tips](/blog/divi-5-speed-optimization-tips/) — what actually moves a mobile score
