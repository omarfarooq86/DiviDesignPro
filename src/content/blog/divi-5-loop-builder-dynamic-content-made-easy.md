---
title: 'Divi 5 Loop Builder: The Complete Guide to Dynamic Content'
description: 'How the Divi 5 Loop Builder works — query types, dynamic content binding, filtering and pagination. Plus the plugins it replaces and the performance trap to avoid.'
date: 2026-06-12
updated: 2026-08-23
category: 'Divi Tips'
featuredImage: '/blog-images/divi-5-loop-builder-dynamic-content-made-easy-ai.webp'
tags:
  - 'divi 5 loop builder'
  - 'divi dynamic content'
  - 'divi custom post type grid'
hasFAQ: true
faqData:
  - question: 'What is the Divi 5 Loop Builder?'
    answer: 'A native feature that repeats a layout you design for every item in a query. You build one card, choose a data source, and Divi generates an instance for every post, product, term or user that matches.'
  - question: 'How is the Loop Builder different from the Divi Blog module?'
    answer: 'The Blog module gives you a fixed card structure with styling options. The Loop Builder lets you design the card from sections, rows, columns and any modules you like, so the layout is not predetermined.'
  - question: 'Does the Loop Builder replace the Theme Builder?'
    answer: 'No, they work together. Theme Builder creates the template — header, footer, archive, single post. The Loop Builder generates the repeating content inside that template.'
  - question: 'Can the Loop Builder use custom post types and custom fields?'
    answer: 'Yes. It queries registered custom post types, and dynamic content binding reaches custom fields, including ACF and Metabox fields, so property listings or event dates work without code.'
  - question: 'Does the Loop Builder work with WooCommerce?'
    answer: 'Yes. Products are a post type, so you can build fully custom product grids with prices, ratings and add-to-cart buttons instead of using the default shop layout.'
  - question: 'Does the Loop Builder slow down a page?'
    answer: 'It can if you let it. Twelve items with eight modules each is 96 modules rendered. Keep the card lean, limit posts per page, and paginate rather than showing everything at once.'
---

The Loop Builder is the feature that moves Divi from a page builder to a site builder. You design one card, point it at a query, and Divi builds the rest — no PHP, no plugin, no compromise on the layout.

> **TL;DR:** Design a card, enable **Loop** on its container, pick a **Query Type**, bind fields with **dynamic content**. It handles posts, custom post types, WooCommerce products, taxonomy terms and users. It replaces most post-grid plugins outright. The trap: a heavy card multiplied by twelve items is a heavy page.

## What It Actually Does

Divi's Blog module has always displayed posts. What it never did was let you decide what a post card *is*. You got an image, a title, an excerpt and a meta line, in that order, with styling controls.

The Loop Builder inverts that. You build the card as a normal Divi layout — a row, two columns, an image module, a heading, a text module, a button, whatever structure you want — then tell Divi to repeat it for every item in a query. The card is yours. Divi just multiplies it.

That difference is why it replaces plugins rather than competing with the Blog module.

## How to Build a Loop

### 1. Design one instance

Build the card as if it's the only one on the page. Real image, real heading, real button. Design it properly at this stage, because you're about to make twelve of them.

Put it in a **row** or a **Group** — that container is what will repeat.

### 2. Enable Loop on the container

Open the container's settings and turn on **Loop**. Divi now treats its contents as a repeating template.

### 3. Choose the Query Type

This is where the Loop Builder earns its name. You're not limited to posts:

| Query Type | What it loops over | Typical use |
|---|---|---|
| **Post Types** | Posts, pages, products, any registered CPT | Blog grids, portfolios, property listings, product grids |
| **Terms** | Categories, tags, custom taxonomies | A category index page, a "browse by topic" block |
| **Users** | WordPress users, filterable by role | Team directories, author pages |

The Terms query is the underused one. A card per category, each showing the term name, description and post count, is a genuinely useful page that used to require a plugin or a template file.

### 4. Set the query parameters

Per query type you'll typically set:

- **Post type** or taxonomy or role
- **Filters** — specific categories, tags, terms, authors
- **Number of items** per page
- **Order and order by** — date, title, menu order, random
- **Offset** — skip the first N, which is how you build a "featured post plus grid" layout without duplicates
- **Exclusions** — leave out the current post on a related-posts block

### 5. Bind the dynamic content

Now replace your placeholder content. Click the **dynamic content** icon on each field and pick the source: post title, featured image, excerpt, permalink, date, author, categories, comment count, or a **custom field**.

Custom fields are the part that unlocks the interesting work. ACF and Metabox fields are reachable, so a property card can display bedrooms, bathrooms and price, and an event card can display a date and venue — all from fields your client fills in on a normal WordPress edit screen.

### 6. Paginate and publish

Add pagination if the query returns more than one page of results, then publish. Every future post that matches the query appears in the layout automatically.

## Where It Goes in a Site

Inside a **Theme Builder** template, most of the time. That's the combination worth understanding:

- **Theme Builder** builds the wrapper — the archive template, the single post template, the header and footer around it
- **Loop Builder** builds the repeating content inside it

So a blog archive is a Theme Builder template containing a Loop Builder row. A single post page is a Theme Builder template that might contain a *second* small loop for related posts. They're complementary, not alternatives.

## What It Replaces

This is the practical argument, and it's the one I'd lead with when talking to a client:

| What you used before | Now |
|---|---|
| A post grid addon plugin | Native loop |
| A filterable portfolio plugin | Loop with a Terms query and category filters |
| A team members plugin with its own CPT | Your own CPT plus a Users or Post Types loop |
| A related posts plugin | A small loop with the current post excluded |
| A custom `archive-{cpt}.php` template | Theme Builder template plus a loop |
| A testimonial rotator plugin | A loop over a testimonials CPT |

## Best Practices

**Style with presets, not per-instance settings.** The card is a template — build it on [option group presets](/blog/et-how-to-stack-nest-mix-and-match-presets-in-divi-5/) so restyling every card is one edit.

**Reference variables for colour and spacing.** Same reasoning. A loop card built on [Design Variables](/blog/divi-5-global-variables-complete-guide/) restyles with the rest of the site.

**Fix the image shape.** This is the single biggest visual improvement to any loop. Set **Aspect Ratio** with **Object Fit: Cover** on the featured image, and every card matches regardless of what got uploaded. [The grid framing techniques](/blog/et-how-to-build-better-blog-portfolio-and-product-grids-with-as/) go through the ratios worth using.

**Use Flexbox for equal-height cards.** Set Align Items on the loop container and stop fighting ragged card bottoms with CSS.

**Test at 390px.** A three-column loop that looks superb on desktop is where mobile layouts go wrong most often. Check the column stacking and the text length at the narrowest width you support.

**Keep the card shallow.** Which brings us to the one real trap.

## The Performance Trap

A loop renders the card once per item. That's obvious and it's still where people get caught.

A card built from a section containing a row containing two columns containing an image, a heading, two text modules, a divider and a button is nine modules. Show twelve items and the page renders **108 modules**. Show 24 and it's 216.

Divi 5 handles that far better than Divi 4 did, and it's still real work. What to do:

- **Flatten the card.** Nine modules is usually four modules with better use of padding.
- **Limit posts per page.** Nine or twelve, with pagination. "Show all 200" is not a design decision, it's a mistake with a scrollbar.
- **Lazy load below the fold** — but not the first row of cards if they're your LCP element.
- **Size the featured images for the card**, not for a full-width hero. A 300px-wide card does not need a 1600px image.

[The Divi 5 speed checklist](/blog/divi-5-speed-optimization-tips/) covers the rest, and image sizing is the item that matters most here.

## My Take: The Loop Builder Isn't a Blog Grid Tool — It's a Reason to Stop Installing Plugins

Here's my one strong opinion: **everybody demos the Loop Builder by making a prettier blog grid, which is the least valuable thing it does. Its real value is that it deletes plugins from your stack, and that matters more every year.**

I've built over 100 Divi sites. On a typical content-heavy build, the Loop Builder has let me remove two or three plugins — a post grid addon, a filterable portfolio plugin, sometimes a testimonial rotator. Each of those was doing one job that the Loop Builder now does natively and, in every case, better, because the card layout was mine instead of theirs.

The reason that's worth more than a nicer grid is the maintenance arithmetic. Every plugin is a permanent liability: an update that can conflict, a developer who can abandon it, a security surface, and assets loading on pages that don't use it. And if it's a **Divi module plugin specifically**, it's also the exact thing that breaks a Divi 5 upgrade — those plugins register modules through the builder API, and when that API was rewritten, the ones without a Divi 5 release started rendering blank sections on the front end while looking fine in the builder.

So the Loop Builder isn't just a feature. It's a way to retire the riskiest category of plugin on a Divi site. Three plugins removed is three fewer things that can turn your next upgrade into a diagnosis session.

My rule when I open an existing Divi site: **list every plugin whose entire job is displaying a list of things.** Post grids, portfolio filters, team directories, testimonial sliders, event lists, property listings. Nearly all of them are a Loop Builder query and an afternoon. Not because the plugins are bad — several are excellent — but because a native feature you already own beats a dependency you have to keep compatible.

The prettier blog grid is a nice side effect. The shorter plugin list is the point.

## Straight Answers

**What is it?**
A native feature that repeats a layout you design for every item in a query.

**How is it different from the Blog module?**
The Blog module fixes the card structure. The Loop Builder lets you build the card yourself.

**Does it replace Theme Builder?**
No. Theme Builder is the template, the loop is the repeating content inside it.

**Custom post types and custom fields?**
Both, including ACF and Metabox fields.

**WooCommerce?**
Yes — products are a post type, so fully custom product grids work.

**Does it slow pages down?**
Only if the card is heavy. Keep it shallow, limit items, paginate.

## The Last Word

The Loop Builder does two things at once: it gives you complete design control over repeating content, and it removes the plugins you were using to get halfway there.

Design the card properly, set the aspect ratio so the images behave, build it on presets and variables, keep it to nine modules or fewer, and paginate. Then go look at your plugin list and see what's now redundant.

[Divi 5](https://www.elegantthemes.com/affiliates/idevaffiliate.php?id=81533) includes the Loop Builder with any active licence — no addon, no extra purchase. If you've got a site running three plugins to display lists of things and you'd like them consolidated into native loops, [that's a satisfying afternoon](#contact).

## Related Reading

- [Divi 5 Global Variables: Complete Guide](/blog/divi-5-global-variables-complete-guide/) — what your loop cards should reference instead of hex codes
- [Better Blog, Portfolio and Product Grids with Aspect Ratio](/blog/et-how-to-build-better-blog-portfolio-and-product-grids-with-as/) — the image framing that makes a loop look finished
- [Divi 5 Speed Optimization Tips](/blog/divi-5-speed-optimization-tips/) — keeping a 12-item loop from becoming a 4MB page
