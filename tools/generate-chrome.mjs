#!/usr/bin/env node
/**
 * generate-chrome.mjs — rewrite sticky chrome (+ footer-nav) from pack chrome.json
 *
 * Usage:
 *   node tools/generate-chrome.mjs [--dry-run] [pack...]
 *
 * No pack args → discover refs/<pack>/chrome.json (or fall back to cf-2018, ifrs-18).
 * Offline / file:// safe. Idempotent via chrome:start/end and footer-nav:start/end markers.
 */

import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const REPO_ROOT = path.resolve(__dirname, '..');
const REFS_DIR = path.join(REPO_ROOT, 'refs');
const DEFAULT_PACKS = ['cf-2018', 'ifrs-18'];

function usageAndExit(code = 1) {
  console.error('Usage: node tools/generate-chrome.mjs [--dry-run] [pack...]');
  process.exit(code);
}

function shortLabel(label) {
  return label.replace(/^\d+\s+/, '');
}

function buildChromeHtml(config, activeFile) {
  const tagsHtml = config.tags
    .map((t) => {
      const active = t.file === activeFile ? ' active' : '';
      return `<a class="tag${active}" href="${t.file}">${t.label}</a>`;
    })
    .join('');

  return [
    '<!-- chrome:start -->',
    '<header class="chrome-bar">',
    '  <div class="chrome-bar-title">',
    `    <a class="chrome-home" href="${config.home.href}">${config.home.label}</a>`,
    `    <span>${config.title}</span>`,
    '    <span class="chrome-bar-actions">',
    '      <span style="font-weight:500;letter-spacing:0;text-transform:none;color:var(--dash)">scroll tags →</span>',
    '    </span>',
    '  </div>',
    '  <nav class="tag-row-wrap" aria-label="Chapters">',
    `    <div class="tag-row">${tagsHtml}</div>`,
    '  </nav>',
    '</header>',
    '<!-- chrome:end -->',
  ].join('\n');
}

function buildFooterHtml(config, activeFile) {
  const tags = config.tags;
  const idx = tags.findIndex((t) => t.file === activeFile);
  if (idx < 0) {
    throw new Error(`active file ${activeFile} not in chrome.json tags`);
  }

  const isMap = tags[idx].id === 'map' || activeFile === 'index.html';
  const isLast = idx === tags.length - 1;

  let inner;
  if (isMap) {
    const next = tags[1];
    if (!next) {
      inner = '<span></span>';
    } else {
      inner = `<span></span><a href="${next.file}">Next: ${shortLabel(next.label)} →</a>`;
    }
  } else if (isLast) {
    const prev = tags[idx - 1];
    inner =
      `<a href="${prev.file}">← Prev: ${shortLabel(prev.label)}</a>` +
      `<a class="mid" href="index.html">Map</a>` +
      `<span></span>`;
  } else {
    const prev = tags[idx - 1];
    const next = tags[idx + 1];
    inner =
      `<a href="${prev.file}">← Prev: ${shortLabel(prev.label)}</a>` +
      `<a class="mid" href="index.html">Map</a>` +
      `<a href="${next.file}">Next: ${shortLabel(next.label)} →</a>`;
  }

  return [
    '<!-- footer-nav:start -->',
    `<nav class="footer-nav">${inner}</nav>`,
    '<!-- footer-nav:end -->',
  ].join('\n');
}

const CHROME_MARKED =
  /<!--\s*chrome:start\s*-->[\s\S]*?<!--\s*chrome:end\s*-->/;
const CHROME_UNMARKED =
  /<header\s+class="chrome-bar"[\s\S]*?<\/header>/;
const FOOTER_MARKED =
  /<!--\s*footer-nav:start\s*-->[\s\S]*?<!--\s*footer-nav:end\s*-->/;
const FOOTER_UNMARKED =
  /<nav\s+class="footer-nav"[\s\S]*?<\/nav>/;

function applyChrome(html, chromeBlock) {
  if (CHROME_MARKED.test(html)) {
    return html.replace(CHROME_MARKED, chromeBlock);
  }
  if (CHROME_UNMARKED.test(html)) {
    return html.replace(CHROME_UNMARKED, chromeBlock);
  }
  // Insert after <body...>
  const bodyOpen = /<body[^>]*>/i;
  if (bodyOpen.test(html)) {
    return html.replace(bodyOpen, (m) => `${m}\n${chromeBlock}`);
  }
  throw new Error('no chrome-bar and no <body> to insert into');
}

function applyFooter(html, footerBlock) {
  if (FOOTER_MARKED.test(html)) {
    return html.replace(FOOTER_MARKED, footerBlock);
  }
  if (FOOTER_UNMARKED.test(html)) {
    return html.replace(FOOTER_UNMARKED, footerBlock);
  }
  // Insert before </main> if present, else before </body>
  if (/<\/main>/i.test(html)) {
    return html.replace(/<\/main>/i, `${footerBlock}\n</main>`);
  }
  if (/<\/body>/i.test(html)) {
    return html.replace(/<\/body>/i, `${footerBlock}\n</body>`);
  }
  throw new Error('no footer-nav insert point (missing </main> and </body>)');
}

function shouldSkipFile(filePath, htmlDirAbs) {
  const rel = path.relative(htmlDirAbs, filePath);
  const parts = rel.split(path.sep);
  if (parts.some((p) => p.startsWith('_archive'))) return true;
  if (parts[0] === 'visuals' || parts[0] === 'assets') return true;
  return false;
}

function loadConfig(pack) {
  const packDir = path.join(REFS_DIR, pack);
  const jsonPath = path.join(packDir, 'chrome.json');
  if (!fs.existsSync(jsonPath)) {
    console.error(`Missing chrome.json: ${jsonPath}`);
    process.exit(1);
  }
  let config;
  try {
    config = JSON.parse(fs.readFileSync(jsonPath, 'utf8'));
  } catch (e) {
    console.error(`Invalid chrome.json ${jsonPath}: ${e.message}`);
    process.exit(1);
  }
  if (!config.tags?.length || !config.htmlDir || !config.home?.href) {
    console.error(`chrome.json incomplete: ${jsonPath}`);
    process.exit(1);
  }
  return { packDir, jsonPath, config };
}

function processPack(pack, dryRun) {
  const { packDir, jsonPath, config } = loadConfig(pack);
  const htmlDirAbs = path.join(packDir, config.htmlDir);
  if (!fs.existsSync(htmlDirAbs)) {
    console.error(`Missing htmlDir: ${htmlDirAbs}`);
    process.exit(1);
  }

  console.log(`\n[${pack}] config ${path.relative(REPO_ROOT, jsonPath)}`);
  let changed = 0;
  let unchanged = 0;

  for (const tag of config.tags) {
    const filePath = path.join(htmlDirAbs, tag.file);
    if (shouldSkipFile(filePath, htmlDirAbs)) {
      console.log(`  skip ${tag.file}`);
      continue;
    }
    if (!fs.existsSync(filePath)) {
      console.error(`Missing HTML: ${filePath}`);
      process.exit(1);
    }

    const original = fs.readFileSync(filePath, 'utf8');
    const chromeBlock = buildChromeHtml(config, tag.file);
    const footerBlock = buildFooterHtml(config, tag.file);
    let next = applyChrome(original, chromeBlock);
    next = applyFooter(next, footerBlock);

    if (next === original) {
      unchanged += 1;
      console.log(`  ok   ${tag.file} (unchanged)`);
    } else {
      changed += 1;
      if (dryRun) {
        console.log(`  would-write ${tag.file}`);
      } else {
        fs.writeFileSync(filePath, next, 'utf8');
        console.log(`  wrote ${tag.file}`);
      }
    }
  }

  console.log(
    `[${pack}] ${dryRun ? 'dry-run ' : ''}changed=${changed} unchanged=${unchanged}`,
  );
  return { changed, unchanged };
}

function discoverPacks() {
  if (!fs.existsSync(REFS_DIR)) return DEFAULT_PACKS;
  const found = fs
    .readdirSync(REFS_DIR, { withFileTypes: true })
    .filter((d) => d.isDirectory())
    .map((d) => d.name)
    .filter((name) => fs.existsSync(path.join(REFS_DIR, name, 'chrome.json')))
    .sort();
  return found.length ? found : DEFAULT_PACKS;
}

function main() {
  const args = process.argv.slice(2);
  let dryRun = false;
  const packs = [];
  for (const a of args) {
    if (a === '--dry-run') dryRun = true;
    else if (a === '-h' || a === '--help') usageAndExit(0);
    else if (a.startsWith('-')) {
      console.error(`Unknown flag: ${a}`);
      usageAndExit(1);
    } else packs.push(a);
  }

  const targets = packs.length ? packs : discoverPacks();
  if (dryRun) console.log('DRY-RUN (no writes)');
  console.log(`Packs: ${targets.join(', ')}`);

  let totalChanged = 0;
  for (const pack of targets) {
    const r = processPack(pack, dryRun);
    totalChanged += r.changed;
  }
  console.log(`\nDone. total ${dryRun ? 'would-change' : 'changed'}=${totalChanged}`);
}

main();
