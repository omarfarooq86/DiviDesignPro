---
title: 'How to Hide a Section in Divi 5 — 4 Methods Explained'
description: 'Learn four ways to hide a section in Divi 5: visibility settings, device-specific hiding, CSS, and Divi Library. Keep your designs safe without deleting anything.'
date: 2026-06-12
category: 'Divi Tips'
featuredImage: '/blog-images/how-to-hide-a-section-in-divi-5-ai.webp'
---

When building with Divi 5, you'll often want to temporarily hide a section — for seasonal promotions, A/B testing, client approvals, or preparing future content. Divi gives you multiple ways to do it **without losing your work**.

## Why Hide Instead of Delete?

Deleting content you might need later creates unnecessary rework. Hiding a section lets you:

- Preserve your design work for future use
- Temporarily remove content from visitors
- Test new layouts safely with live backups
- Schedule content for future campaigns
- Keep alternate versions of sections

## Method 1: Built-in Visibility Settings (Recommended)

This is the simplest approach for most users.

1. Open the page in the **Divi 5 Visual Builder**
2. Hover over the section and click the **Settings icon**
3. Navigate to the **Visibility options** panel
4. **Disable the section**

The section remains visible inside the builder but disappears from the front end. It's fast, requires no code, and preserves all content and styling.

## Method 2: Hide on Specific Devices

Sometimes you only want to hide a section on mobile, tablet, or desktop. For example, a large hero section may work beautifully on desktop but overwhelm a phone screen.

1. Open section settings
2. Go to Visibility options
3. Choose which devices to hide on: **Desktop**, **Tablet**, or **Mobile**
4. Save your changes

Divi automatically shows or hides the section based on the visitor's device.

## Method 3: CSS-Based Hiding

For advanced scenarios, CSS gives you precise control. Assign a custom CSS class to the section:

```css
.hidden-section {
    display: none;
}
```

The section stays in the page structure but becomes invisible. This is ideal for conditional display scenarios, custom JavaScript interactions, and advanced visibility control.

## Method 4: Save to the Divi Library

If you're hiding content long-term, consider saving it to the **Divi Library** instead.

**Benefits:**
- Keeps your active page clean and clutter-free
- Creates reusable design assets for other projects
- Makes future restoration instant

After saving, you can safely remove the section from the page and reinsert it whenever needed.

## Common Use Cases

| Scenario | Best Method |
|---|---|
| Seasonal holiday banners | Visibility settings — toggle on/off yearly |
| Website redesigns | Divi Library — keep originals as backups |
| A/B testing layouts | CSS or visibility — show different versions to segments |
| Client approval workflows | Visibility — hide until approved |
| Upcoming feature launches | Visibility — prepare now, reveal later |

## Troubleshooting

**Section still appears after hiding?** Check device-specific visibility settings, custom CSS overrides, caching plugins, and your browser cache.

**Section disappeared in the builder?** Verify you haven't accidentally deleted it. Hidden sections should still appear inside the Visual Builder.

**Changes not showing on the front end?** Clear Divi cache, website cache, CDN cache, and browser cache — then refresh.

## Best Practice

For most users, **Divi 5's built-in Visibility settings are the recommended solution**. They're easy, code-free, and allow instant restoration.

Use CSS-based hiding only when you need advanced control or custom functionality that the built-in options don't cover.

## Related Posts

- [Sticky Sidebar Not Working in Divi? Here's the Fix](/blog/sticky-sidebar-not-working-in-divi-fix/) — Another common Divi layout issue with a simple fix
- [Divi 5 Loop Builder: Dynamic Content Made Easy](/blog/divi-5-loop-builder-dynamic-content-made-easy/) — Build layouts that adapt automatically instead of hiding sections manually
