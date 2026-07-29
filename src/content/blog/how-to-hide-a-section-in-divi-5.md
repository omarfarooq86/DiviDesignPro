---
title: 'How to Hide a Section in Divi 5'
description: 'Learn multiple ways to hide a section in Divi 5 without deleting it. Covers visibility settings, device-specific hiding, CSS methods, and library-saving for future use.'
date: 2026-06-12
category: 'Divi Tips'
featuredImage: 'https://dividesignpro.com/wp-content/uploads/2026/06/gemini_generated_image_35g8ih35g8ih35g8-clean-1080x675.webp'
---

When building a website with Divi 5, there are many situations where you may want to temporarily hide a section without deleting it. Whether you're working on a new design, running seasonal promotions, testing layouts, or preparing content for a future launch, Divi makes it easy to hide sections from visitors while keeping them available inside the builder.

## Why Hide a Section Instead of Deleting It?

Hiding a section allows you to preserve your design work, temporarily remove content from visitors, test new layouts safely, schedule future content updates, keep backup versions of sections, and run seasonal promotions without rebuilding them later.

Instead of recreating everything from scratch, you can simply unhide the section whenever needed.

## Method 1: Disable a Section Using Visibility Settings

This is the most common method for hiding a section.

1. Open the page where your section is located and launch the Divi 5 Visual Builder.
2. Hover over the section you want to hide and click the Settings icon.
3. In the settings panel, locate the Visibility settings.
4. Turn off the visibility option for the section.

Once disabled, the section will remain inside the builder but will not appear on the front end of the website.

**Benefits:** Fast and simple, no code required, easy to restore later, preserves all content and styling.

## Method 2: Hide a Section on Specific Devices

Sometimes you only want to hide a section on mobile, tablet, or desktop. For example, a large hero section may look great on desktop but not on mobile.

**Steps:**
1. Open the section settings
2. Go to Visibility options
3. Choose which devices should hide the section (Desktop, Tablet, Mobile)
4. Save your changes

Divi will automatically display or hide the section based on the visitor's device.

## Method 3: Hide a Section Using CSS

Advanced users may prefer using CSS. You can assign a custom CSS class to the section and hide it using code:

```css
.hidden-section {
    display: none;
}
```

The section remains in the page structure but becomes invisible to visitors. Use CSS for conditional display scenarios, custom development projects, dynamic JavaScript interactions, and advanced visibility control.

## Method 4: Save Sections for Future Use

If you're hiding content for a long period, consider saving it to the Divi Library. This keeps pages clean, reduces clutter in the builder, creates reusable design assets, and makes future updates easier.

After saving the section to the library, you can safely remove it from the page and reinsert it whenever needed.

## Common Use Cases

- **Seasonal Promotions** – Hide holiday banners after a campaign ends and reactivate them next year
- **Website Redesigns** – Build replacement sections while keeping original versions as backups
- **A/B Testing** – Create multiple versions of a section and selectively display them during testing
- **Client Approval Workflows** – Keep unfinished sections hidden until clients approve them
- **Upcoming Features** – Prepare future content before launch and reveal it when ready

## Best Practice

For most users, the built-in Visibility settings in Divi 5 are the recommended solution. They are easy to use, require no code, and allow sections to be restored instantly whenever needed. Use CSS-based hiding only when you need advanced control or custom functionality.

Hiding a section in Divi 5 is a simple but powerful feature that can improve your workflow and make website management easier. By using Divi 5's visibility options, device-specific controls, and reusable design features, you can build websites more efficiently while keeping your layouts organized and flexible.
