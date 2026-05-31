import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const curriculum = defineCollection({
  loader: glob({ pattern: '**/*.{md,mdx}', base: './src/content/curriculum' }),
  schema: z.object({
    title: z.string(),
    stationNumber: z.number(),
    line: z.enum([
      'Foundation Way',
      'Math & Quantum Hub',
      'Quantum Trunk',
      'Advanced QFT Loop',
      'Classical Branch',
      'Gravitational Spur',
    ]),
    date: z.coerce.date(),
    backdated: z.boolean().default(true),
    prerequisites: z.array(z.number()).default([]),
    extendsTo: z.array(z.number()).default([]),
    classReportTitle: z.string(),
  }),
});

const essays = defineCollection({
  loader: glob({ pattern: '**/*.{md,mdx}', base: './src/content/essays' }),
  schema: z.object({
    title: z.string(),
    subtitle: z.string().optional(),
    date: z.coerce.date(),
    backdated: z.boolean().default(false),
    section: z.enum(['field-notes', 'method']),
    subsection: z.enum([
      'work-post',
      'standalone',
      'reference',
      'method-essay',
    ]),
    voice: z.enum(['donkey', 'paper']).default('donkey'),
    status: z.enum(['ready', 'draft', 'placeholder', 'reference']).default('ready'),
    workPhase: z.number().optional(),
    series: z.enum(['paper-1', 'paper-2-3']).default('paper-1'),
    featured: z.boolean().default(false),
  }),
});

const resultsSchema = z.object({
  title: z.string(),
  resultNumber: z.number().min(1).max(5),
  scaling: z.string().optional(),
  status: z.enum(['clean', 'empirical', 'open', 'conditional', 'headline']).default('clean'),
  summary: z.string(),
});

const results = defineCollection({
  loader: glob({ pattern: '**/*.{md,mdx}', base: './src/content/results' }),
  schema: resultsSchema,
});

const resultsPaperOne = defineCollection({
  loader: glob({ pattern: '**/*.{md,mdx}', base: './src/content/results-paper-one' }),
  schema: resultsSchema,
});

const calibration = defineCollection({
  loader: glob({ pattern: '**/*.{md,mdx}', base: './src/content/calibration' }),
  schema: z.object({
    title: z.string(),
    date: z.coerce.date(),
    phase: z.string(),
    prediction: z.string(),
    outcome: z.enum(['confirmed', 'refuted', 'pending', 'partial']),
    probabilityBefore: z.number().min(0).max(1).optional(),
    probabilityAfter: z.number().min(0).max(1).optional(),
    notes: z.string().optional(),
  }),
});

const phaseMemos = defineCollection({
  loader: glob({ pattern: '**/*.{md,mdx}', base: './src/content/phase-memos' }),
  schema: z.object({
    title: z.string(),
    date: z.coerce.date(),
    phases: z.string(),
    status: z.enum(['complete', 'in-progress']).default('complete'),
  }),
});

const papers = defineCollection({
  loader: glob({ pattern: '**/*.{md,mdx}', base: './src/content/papers' }),
  schema: z.object({
    title: z.string(),
    kind: z.enum(['manuscript', 'appendix', 'reviewer-note']),
    paperNumber: z.number(),
    order: z.number().default(0),
    subtitle: z.string().optional(),
  }),
});

export const collections = {
  curriculum,
  essays,
  results,
  'results-paper-one': resultsPaperOne,
  calibration,
  'phase-memos': phaseMemos,
  papers,
};
