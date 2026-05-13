import { defineCollection, z } from 'astro:content';

const curriculum = defineCollection({
  type: 'content',
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
  type: 'content',
  schema: z.object({
    title: z.string(),
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
  }),
});

const results = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    resultNumber: z.number().min(1).max(5),
    scaling: z.string().optional(),
    status: z.enum(['clean', 'empirical', 'open']).default('clean'),
    summary: z.string(),
  }),
});

const calibration = defineCollection({
  type: 'content',
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
  type: 'content',
  schema: z.object({
    title: z.string(),
    date: z.coerce.date(),
    phases: z.string(),
    status: z.enum(['complete', 'in-progress']).default('complete'),
  }),
});

export const collections = {
  curriculum,
  essays,
  results,
  calibration,
  'phase-memos': phaseMemos,
};
