#!/usr/bin/env node
// Populate curriculum MDX shells with body content from raw .md files in
// .curriculum-from-drive/. Preserves the existing frontmatter from the .mdx
// shell. Strips em-dashes from the body (project-wide rule). Skips files that
// already have substantive content (>= 100 lines) so we don't clobber the 5
// already-populated MDX files.

import { readFile, writeFile, readdir, stat } from 'node:fs/promises';
import { existsSync } from 'node:fs';
import path from 'node:path';

const repoRoot = path.resolve(new URL('..', import.meta.url).pathname);
const SRC = path.join(repoRoot, '.curriculum-from-drive');
const DEST = path.join(repoRoot, 'src/content/curriculum');

if (!existsSync(SRC)) {
  console.error(`Missing source dir: ${SRC}`);
  process.exit(1);
}

function scrubEmDashes(s) {
  return s
    .replace(/ — /g, '; ')
    .replace(/^— /gm, 'That is, ')
    .replace(/—/g, '-');
}

function stripFirstH1(body) {
  // The .md files start with "# Title". The MDX page renders its own
  // <h1> from the frontmatter classReportTitle, so drop the duplicate.
  return body.replace(/^#\s+[^\n]*\n+/, '');
}

function splitFrontmatter(text) {
  const m = text.match(/^---\n([\s\S]*?)\n---\n?([\s\S]*)$/);
  if (!m) return { frontmatter: '', body: text };
  return { frontmatter: m[1], body: m[2] };
}

const sources = (await readdir(SRC)).filter((f) => f.endsWith('.md'));
let updated = 0;
let skippedExisting = 0;
let skippedNoShell = 0;

for (const md of sources) {
  const slug = md.replace(/\.md$/, '');
  const targetPath = path.join(DEST, `${slug}.mdx`);

  if (!existsSync(targetPath)) {
    console.warn(`  no shell for ${slug} — skipping`);
    skippedNoShell++;
    continue;
  }

  const targetText = await readFile(targetPath, 'utf8');
  const { frontmatter, body: existingBody } = splitFrontmatter(targetText);
  const existingLines = existingBody.split('\n').length;

  if (existingLines >= 100) {
    skippedExisting++;
    continue;
  }

  const rawBody = await readFile(path.join(SRC, md), 'utf8');
  const cleanBody = scrubEmDashes(stripFirstH1(rawBody)).trimEnd();

  const newText = `---\n${frontmatter}\n---\n\n${cleanBody}\n`;
  await writeFile(targetPath, newText);
  updated++;
}

console.log(`Updated ${updated} curriculum files.`);
console.log(`Skipped ${skippedExisting} (already populated).`);
if (skippedNoShell) console.log(`Skipped ${skippedNoShell} (no MDX shell).`);
