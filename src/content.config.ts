import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const blogCollection = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/blog' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    date: z.date(),
    updated: z.date().optional(),
    category: z.string().default('Divi Tips'),
    tags: z.array(z.string()).optional(),
    featuredImage: z.string().optional(),
    ogImage: z.string().optional(),
    draft: z.boolean().default(false),
    hasFAQ: z.boolean().optional(),
    faqData: z.array(z.object({ question: z.string(), answer: z.string() })).optional(),
  }),
});

const portfolioCollection = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/portfolio' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    category: z.string(),
    client: z.string().optional(),
    url: z.string().url().optional(),
    image: z.string(),
    images: z.array(z.string()).optional(),
    order: z.number().default(0),
  }),
});

export const collections = {
  blog: blogCollection,
  portfolio: portfolioCollection,
};
