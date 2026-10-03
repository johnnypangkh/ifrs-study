"""Read-only structural / QA audit of the IAS 2 pack chapters.

Mirrors the automated checks in the ifrs-teaching-body-qa skill:
cite grammar, Illus shape, neutral peers, markup, densify counts,
title-essence leads, flowery titles, hyperlink targets.
"""
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parent.parent
CHAPTERS = [f"ch0{i}.html" for i in range(1, 7)]
FLOWERY = re.compile(r"journey|unlock value|key takeaway|at a glance|insights for|best practice tip|game.?changer|story|ritual", re.I)
LEAD_FAIL = re.compile(r"^(IFRS 15|DTT|PwC|EY|KPMG|Official|IAS 2)\s*[:.]?$")


def load(name):
    return BeautifulSoup((ROOT / name).read_text(encoding="utf-8"), "lxml")


def all_ids():
    ids = defaultdict(set)
    for name in CHAPTERS + ["index.html"]:
        for tag in load(name).find_all(attrs={"id": True}):
            ids[name].add(tag["id"])
    return ids


def audit(name, ids, verbose):
    soup = load(name)
    art = soup.find("article") or soup
    out = []
    p = out.append
    p(f"\n===== {name} =====")

    heads = art.find_all(["h2", "h3", "h4"])
    p(f"headings: {len(heads)}")
    if verbose:
        for h in heads:
            hid = h.get("id") or (h.parent.get("id") if h.parent else "")
            p(f"  {h.name} [{hid}] {h.get_text(' ', strip=True)[:110]}")

    cites = art.select(".cite")
    p(f"cite chips: {len(cites)}  by class: {dict(Counter(c for s in cites for c in s.get('class', []) if c.startswith('cite-')))}")
    house_only = [c for c in cites if c.select_one('.cite-house') and c.get_text(strip=True) in ('PwC', 'DTT', 'EY', 'KPMG')]
    sect = [c.get_text(' ', strip=True) for c in cites if '§' in c.get_text()]
    bad_ey = [c.get_text(' ', strip=True) for c in cites if 'cite-ey' in c.get('class', []) and 'IGAAP 2026' not in c.get_text()]
    bad_off = [c.get_text(' ', strip=True) for c in cites if 'cite-official' in c.get('class', []) and not re.match(r'^(IAS|IFRS|IFRIC|SIC|CF|Conceptual)', c.get_text(strip=True))]
    bad_kpmg = [c.get_text(' ', strip=True) for c in cites if 'cite-kpmg' in c.get('class', []) and 'Insights 2019/20' not in c.get_text()]
    bad_pwc = [c.get_text(' ', strip=True) for c in cites if 'cite-pwc' in c.get('class', []) and 'MOA 2020' not in c.get_text()]
    bad_dtt = [c.get_text(' ', strip=True) for c in cites if 'cite-dtt' in c.get('class', []) and 'A11 2022' not in c.get_text()]
    p(f"  house-only: {len(house_only)}  §-in-chip: {sect[:5]}  EY-not-IGAAP: {bad_ey[:5]}")
    p(f"  official-odd: {bad_off[:8]}  kpmg-odd: {bad_kpmg[:5]}  pwc-odd: {bad_pwc[:5]}  dtt-odd: {bad_dtt[:5]}")
    hk = [t for t in art.find_all(string=re.compile(r'HKAS|HKFRS'))]
    p(f"  HKAS/HKFRS on UI text: {len(hk)} {[t.strip()[:60] for t in hk[:3]]}")

    strips = art.select(".worked-strip")
    illus_titles = [t for t in art.find_all(string=re.compile(r'Illustration:\s*\d'))]
    p(f"worked-strips: {len(strips)}  'Illustration: N' strings: {len(illus_titles)}")
    lone = [t.strip()[:60] for t in illus_titles if not t.find_parent(class_='worked-strip')]
    if lone:
        p(f"  ILLUS NOT IN STRIP: {lone}")
    for s in strips:
        title_el = s.select_one('.worked-strip-title')
        title = title_el.find('strong').get_text(' ', strip=True) if title_el and title_el.find('strong') else (title_el.get_text(' ', strip=True)[:80] if title_el else '?')
        grid = s.select_one('.worked-strip-grid')
        peers = grid.find_all('div', class_='box', recursive=False) if grid else []
        labels = [b.select_one('.box-title').get_text(strip=True) if b.select_one('.box-title') else '?' for b in peers]
        colored = [b.get('class') for b in s.select('.box') if set(b.get('class', [])) & {'ok', 'warn', 'danger'}]
        lis = s.select('.worked-strip-grid li')
        chars = sum(len(li.get_text(' ', strip=True)) for li in lis)
        if not lis and grid:
            chars = len(grid.get_text(' ', strip=True))
        body_cites = len(grid.select('.cite')) if grid else 0
        title_cites = len(title_el.select('.cite')) if title_el else 0
        extras = [c.name + ('.' + '.'.join(c.get('class', [])) if c.get('class') else '') for c in s.find_all(recursive=False) if c is not title_el and c is not grid]
        has_visual = bool(s.select('table, svg, .mini-flow, .flow, .diag')) or any('table' in e for e in extras)
        thin = (len(lis) <= 5 or chars < 350)
        flag = []
        if thin: flag.append('THIN')
        if colored: flag.append(f'COLOURED{colored}')
        if body_cites: flag.append(f'BODY-CITES{body_cites}')
        if not title_cites: flag.append('NO-TITLE-CITES')
        if FLOWERY.search(title): flag.append('FLOWERY?')
        p(f"  [{s.get('id','-')}] {title[:90]} | peers={labels} li={len(lis)} chars={chars} chips={title_cites} vis={'Y' if has_visual else 'n'} extras={extras} {' '.join(flag)}")

    pbody_ul = len(re.findall(r'<p class="box-body">\s*<(ul|ol)', (ROOT / name).read_text()))
    p(f"<p class=box-body><ul>: {pbody_ul}")

    tables = art.find_all('table')
    p(f"tables: {len(tables)} (in strips: {sum(1 for t in tables if t.find_parent(class_='worked-strip'))})")

    leads = [s.get_text(' ', strip=True) for s in art.find_all('strong') if LEAD_FAIL.match(s.get_text(' ', strip=True))]
    p(f"title-essence fails: {leads[:6]}")
    flowery = [h.get_text(' ', strip=True)[:80] for h in heads if FLOWERY.search(h.get_text())]
    p(f"flowery heading cues: {flowery}")

    plain_see = []
    for t in art.find_all(string=re.compile(r'\b(see|See)\s+(Illustration\s+)?\d+\.\d+')):
        if not t.find_parent('a'):
            plain_see.append(t.strip()[:80])
    p(f"plain 'see N.M' not linked: {len(plain_see)} {plain_see[:5]}")

    broken = []
    for a in soup.find_all('a', href=True):
        href = a['href']
        if '#' not in href or href.startswith('http'):
            continue
        page, frag = href.split('#', 1)
        page = page or name
        page = page.split('/')[-1]
        if page in ids and frag not in ids[page]:
            broken.append(href)
    p(f"broken anchors: {broken}")

    iframe = soup.find('iframe')
    p(f"iframe: {iframe.get('src') if iframe else None}")
    return "\n".join(out)


if __name__ == "__main__":
    verbose = "-v" in sys.argv
    ids = all_ids()
    for ch in CHAPTERS:
        print(audit(ch, ids, verbose))
