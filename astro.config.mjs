// @ts-check
import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';
import vercel from '@astrojs/vercel';

// Posts marked `noindex: true` in their frontmatter. Kept here as well so they
// are not advertised in the sitemap — a noindex URL in a sitemap is a
// contradiction, and removing them is the point of the exercise.
const noindexPosts = [
  'et-divi-5-11-release-notes',
  'et-divi-5-product-highlight-divi-essential',
  'et-how-to-customize-the-divi-5-builder-interface-with-workspace',
  'et-how-to-stack-nest-mix-and-match-presets-in-divi-5',
  'et-large-quotes-for-divi-5',
  'et-part-10-of-mastering-flexbox-best-practices-helpful-tips',
  'et-part-9-of-mastering-flexbox-creating-responsive-columns-with',
  'et-creative-variable-font-setting-combinations',
];

// https://astro.build/config
export default defineConfig({
  site: 'https://www.dividesignpro.com',
  integrations: [
    sitemap({
      // Exclude paginated archives, category listings and noindexed posts: all
      // thin, and all competing for crawl budget on a low-authority domain.
      filter: (page) =>
        !page.includes('/category/') &&
        !/\/blog\/page\/\d+\/?$/.test(page) &&
        !noindexPosts.some((slug) => page.includes(`/blog/${slug}/`)),
      changefreq: 'weekly',
      priority: 0.7,
      lastmod: new Date(),
    }),
  ],
  output: 'static',
  adapter: vercel({
    webAnalytics: { enabled: true },
  }),
  build: {
    inlineStylesheets: 'auto',
  },
  trailingSlash: 'always',
});
