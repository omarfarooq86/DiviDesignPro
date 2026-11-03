// @ts-check
import fs from 'node:fs';
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

// Real content dates, read straight from the markdown frontmatter.
// Previously every URL carried the build timestamp as `lastmod`, which tells
// Google all 48 pages changed on every deploy — and trains it to ignore the
// signal entirely. Pages with no real date get no lastmod at all.
const blogDir = new URL('./src/content/blog/', import.meta.url);
const contentDates = new Map();

for (const file of fs.readdirSync(blogDir)) {
  if (!file.endsWith('.md')) continue;
  const frontmatter = fs
    .readFileSync(new URL(file, blogDir), 'utf8')
    .match(/^---\r?\n([\s\S]*?)\r?\n---/)?.[1];
  if (!frontmatter) continue;

  const date =
    frontmatter.match(/^updated:\s*(\d{4}-\d{2}-\d{2})/m)?.[1] ??
    frontmatter.match(/^date:\s*(\d{4}-\d{2}-\d{2})/m)?.[1];
  if (date) contentDates.set(`/blog/${file.replace(/\.md$/, '')}/`, date);
}

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
      serialize: (item) => {
        const date = contentDates.get(new URL(item.url).pathname);
        if (date) item.lastmod = `${date}T00:00:00.000Z`;
        else delete item.lastmod;
        return item;
      },
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
