import { defineCollection, z } from 'astro:content';

const editionsCollection = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    section: z.enum(['front-page', 'world', 'tech', 'business', 'culture', 'opinion']),
    author: z.string(),
    date: z.string(),
    confidence: z.enum(['high', 'medium', 'speculative']),
    size: z.enum(['major', 'secondary', 'standard']).optional(),
    columns: z.number().optional(),
    predictionBasis: z.string().optional(),
  }),
});

export const collections = {
  'editions': editionsCollection,
};
