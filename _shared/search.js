/* Chapter, map, abbreviations, and homepage note search.
   Reads window.HOMEPAGE_SEARCH_INDEX. Does not name packs or chapters.
   On a chapter page, exact hits from that page come first, then exact hits
   from other pages, then the same split for close matches.
   Map and abbreviations pages use the same search bar as a chapter. */
(function () {
  var PAGE_SIZE = 5;

  function escapeHtml(value) {
    return String(value)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;');
  }

  function queryWords(query) {
    return String(query).toLowerCase().replace(/[’‘]/g, "'").match(/[a-z0-9']+/g) || [];
  }

  function wordSpans(sentence) {
    var spans = [];
    var re = /[A-Za-z0-9’‘']+/g;
    var match;
    while ((match = re.exec(sentence))) {
      spans.push({
        start: match.index,
        end: match.index + match[0].length,
        norm: match[0].toLowerCase().replace(/[’‘]/g, "'")
      });
    }
    return spans;
  }

  function pluralS(a, b) {
    if (a === b) return false;
    var short = a.length < b.length ? a : b;
    var long = a.length < b.length ? b : a;
    return long.length === short.length + 1 && long.slice(0, short.length) === short && long.charAt(long.length - 1) === 's' && short.length >= 3;
  }

  function tenseStems(word) {
    var stems = [];
    if (word.length > 6 && word.slice(-3) === 'ing') {
      var base = word.slice(0, -3);
      stems.push(base, base + 'e');
    }
    if (word.length > 5 && word.slice(-2) === 'ed') {
      stems.push(word.slice(0, -2), word.slice(0, -1));
    }
    if (word.length > 5 && word.slice(-2) === 'es') {
      stems.push(word.slice(0, -2), word.slice(0, -1));
    }
    if (word.length > 4 && word.slice(-1) === 's' && word.slice(-2) !== 'ss') {
      stems.push(word.slice(0, -1));
    }
    return stems;
  }

  function sameTense(a, b) {
    if (a === b || pluralS(a, b)) return false;
    var aStems = tenseStems(a);
    var bStems = tenseStems(b);
    if (aStems.indexOf(b) !== -1 || bStems.indexOf(a) !== -1) return true;
    for (var i = 0; i < aStems.length; i++) {
      if (aStems[i].length >= 4 && bStems.indexOf(aStems[i]) !== -1) return true;
    }
    return false;
  }

  function oneTypo(a, b) {
    if (a === b || a.length < 5 || b.length < 5 || Math.abs(a.length - b.length) > 1) return false;
    if (a.length === b.length) {
      var diff = 0;
      for (var i = 0; i < a.length; i++) {
        if (a.charAt(i) !== b.charAt(i) && ++diff > 1) return false;
      }
      return diff === 1;
    }
    var short = a.length < b.length ? a : b;
    var long = a.length < b.length ? b : a;
    var i = 0;
    var j = 0;
    var diff = 0;
    while (i < short.length && j < long.length) {
      if (short.charAt(i) === long.charAt(j)) {
        i++;
        j++;
      } else {
        diff++;
        j++;
        if (diff > 1) return false;
      }
    }
    return true;
  }

  function windowKind(qWords, got) {
    if (qWords.length !== got.length) return '';
    var changed = 0;
    var typos = 0;
    for (var i = 0; i < qWords.length; i++) {
      if (qWords[i] === got[i]) continue;
      changed++;
      if (pluralS(qWords[i], got[i]) || sameTense(qWords[i], got[i])) continue;
      if (oneTypo(qWords[i], got[i])) {
        typos++;
        if (typos > 1) return '';
        continue;
      }
      return '';
    }
    if (!changed) return 'exact';
    return 'close';
  }

  function classifyText(text, qWords) {
    var words = wordSpans(text).map(function (span) { return span.norm; });
    var close = false;
    for (var i = 0; i + qWords.length <= words.length; i++) {
      var kind = windowKind(qWords, words.slice(i, i + qWords.length));
      if (kind === 'exact') return 'exact';
      if (kind === 'close') close = true;
    }
    return close ? 'close' : '';
  }

  function proseSentences(text) {
    var source = String(text).replace(/\s+/g, ' ').trim();
    source = source.replace(/(·\s*(?:section\s+[\d.]+|para(?:graph)?\s+[A-Z0-9.\-–]+|\d+(?:\.\d+)*))\s+(?=[A-Z])/g, '$1. ');
    var parts = source.split(/(?<=[.!?])\s+(?=[A-Z])/);
    var sentences = [];
    for (var i = 0; i < parts.length; i++) {
      var sentence = parts[i].trim();
      var lead = sentence.match(/^(?:.*·\s*(?:section\s+[\d.]+|para(?:graph)?\s+\S+|\d[\d.]*))\.?\s+/);
      if (lead && sentence.length - lead[0].length > 40) sentence = sentence.slice(lead[0].length).trim();
      var words = sentence.match(/[A-Za-z]{4,}/g) || [];
      if (sentence.indexOf('·') !== -1 && words.length < 6) continue;
      if (sentence) sentences.push(sentence);
    }
    return sentences;
  }

  function twoSentences(text, qWords) {
    var sentences = proseSentences(text);
    var index = -1;
    for (var i = 0; i < sentences.length; i++) {
      if (classifyText(sentences[i], qWords)) {
        index = i;
        break;
      }
    }
    if (index < 0) {
      var fallback = String(text).replace(/\s+/g, ' ').trim();
      return fallback ? [fallback] : [];
    }
    if (index + 1 < sentences.length) return [sentences[index], sentences[index + 1]];
    if (index > 0) return [sentences[index - 1], sentences[index]];
    return [sentences[index]];
  }

  var CHROME_PAGE = /([^/]+)\/draft-v1-linked\/(?:(ch\d+)|index|abbreviations)\.html$/i;

  function pageKey() {
    var path = String(location.pathname || '').replace(/\\/g, '/');
    var match = path.match(CHROME_PAGE);
    if (!match || !match[2]) return '';
    return match[1] + '/' + match[2].toLowerCase();
  }

  function showsChromeSearch() {
    var path = String(location.pathname || '').replace(/\\/g, '/');
    return CHROME_PAGE.test(path);
  }

  function hitKey(href) {
    var path = String(href || '').split('#')[0].replace(/\\/g, '/');
    var match = path.match(/([^/]+)\/draft-v1-linked\/(ch\d+)\.html$/i);
    if (!match) return '';
    return match[1] + '/' + match[2].toLowerCase();
  }

  function hrefForHere(indexHref) {
    var bits = String(indexHref).split('#');
    var path = bits[0];
    var hash = bits[1] ? '#' + bits[1] : '';
    var target = path.match(/([^/]+)\/draft-v1-linked\/(ch\d+\.html)$/i);
    if (!target) return indexHref;
    var loc = String(location.pathname || '').replace(/\\/g, '/');
    var here = loc.match(CHROME_PAGE);
    if (here) {
      if (here[1].toLowerCase() === target[1].toLowerCase()) return target[2] + hash;
      return '../../' + target[1] + '/draft-v1-linked/' + target[2] + hash;
    }
    // homepage/*.html is one directory under the site root, on GitHub Pages
    // (/ifrs-study/homepage/) and on OneDrive (.../ifrs-website-refs/refs/homepage/).
    // A stored ../../ link leaves that root and 404s at johnnypangkh.github.io.
    if (/\/homepage\/[^/]+$/i.test(loc)) {
      return '../' + target[1] + '/draft-v1-linked/' + target[2] + hash;
    }
    return indexHref;
  }

  function markSentence(sentence, qWords) {
    var spans = wordSpans(sentence);
    var ranges = [];
    for (var i = 0; i + qWords.length <= spans.length; i++) {
      var got = [];
      for (var j = 0; j < qWords.length; j++) got.push(spans[i + j].norm);
      if (!windowKind(qWords, got)) continue;
      ranges.push([spans[i].start, spans[i + qWords.length - 1].end]);
      i += qWords.length - 1;
    }
    var html = '';
    var cursor = 0;
    ranges.forEach(function (range) {
      html += escapeHtml(sentence.slice(cursor, range[0]));
      html += '<mark class="result-mark">' + escapeHtml(sentence.slice(range[0], range[1])) + '</mark>';
      cursor = range[1];
    });
    html += escapeHtml(sentence.slice(cursor));
    return html;
  }

  function close(popover) {
    if (!popover) return;
    popover.hidden = true;
    popover.innerHTML = '';
  }

  function render(popover, hits, page, query) {
    if (!popover) return;
    if (!hits || !hits.length) {
      close(popover);
      return;
    }
    var pages = Math.ceil(hits.length / PAGE_SIZE);
    if (page >= pages) page = 0;
    var start = page * PAGE_SIZE;
    var slice = hits.slice(start, start + PAGE_SIZE);
    var qWords = queryWords(query);
    var html = slice.map(function (hit) {
      var sentences = hit.sentences.map(function (sentence) {
        return '<p class="search-hit-sentence">' + markSentence(sentence, qWords) + '</p>';
      }).join('');
      return '<a class="search-hit" href="' + escapeHtml(hrefForHere(hit.href)) + '">' +
        '<div class="search-hit-chapter">' + escapeHtml(hit.chapter) + '</div>' +
        sentences + '</a>';
    }).join('');
    if (pages > 1) {
      html += '<div class="search-pager"><span class="search-page-label">' + (page + 1) + ' of ' + pages +
        '</span><button class="search-next" type="button">next</button></div>';
    }
    popover.innerHTML = html;
    popover.hidden = false;
    var next = popover.querySelector('.search-next');
    if (next) {
      next.addEventListener('click', function () {
        render(popover, hits, (page + 1) % pages, query);
      });
    }
  }

  function hits(query) {
    var qWords = queryWords(query);
    var index = window.HOMEPAGE_SEARCH_INDEX || [];
    var here = pageKey();
    var exactHere = [];
    var exactOther = [];
    var closeHere = [];
    var closeOther = [];
    if (!qWords.length) return [];
    for (var i = 0; i < index.length; i++) {
      var entry = index[i];
      if (!entry || !entry.text || !entry.chapter || !entry.href) continue;
      var kind = classifyText(entry.text, qWords);
      if (!kind) continue;
      var hit = {
        chapter: entry.chapter,
        href: entry.href,
        sentences: twoSentences(entry.text, qWords)
      };
      var mine = here && hitKey(entry.href) === here;
      if (kind === 'exact') (mine ? exactHere : exactOther).push(hit);
      else (mine ? closeHere : closeOther).push(hit);
    }
    return exactHere.concat(exactOther, closeHere, closeOther);
  }

  function ensureChromeSearch() {
    if (!showsChromeSearch()) return;
    var bar = document.querySelector('header.chrome-bar');
    if (!bar) return;
    var box = document.querySelector('.chapter-search');
    if (!box) {
      box = document.createElement('div');
      box.className = 'chapter-search';
      box.innerHTML = '<label class="chapter-search-label" for="chapterSearch">Search</label>' +
        '<div class="chapter-search-row">' +
        '<input class="chapter-search-input" id="chapterSearch" type="search" autocomplete="off" />' +
        '<button class="chapter-search-clear" id="chapterSearchClear" type="button">clear</button>' +
        '</div>' +
        '<div class="search-popover" id="chapterSearchPopover" hidden></div>';
    }
    if (box.parentNode !== bar) bar.appendChild(box);
  }

  function mountChapter() {
    ensureChromeSearch();
    var input = document.getElementById('chapterSearch');
    var clearButton = document.getElementById('chapterSearchClear');
    var popover = document.getElementById('chapterSearchPopover');
    if (!input || !popover) return;
    function run() {
      var query = input.value.trim().toLowerCase();
      if (!query) {
        close(popover);
        return;
      }
      render(popover, hits(query), 0, query);
    }
    input.addEventListener('input', run);
    if (clearButton) {
      clearButton.addEventListener('click', function () {
        input.value = '';
        close(popover);
      });
    }
  }

  function mountHome() {
    var select = document.getElementById('standardSelect');
    var search = document.getElementById('standardSearch');
    var clearSearch = document.getElementById('searchClear');
    var results = document.getElementById('searchResults');
    var popover = document.getElementById('searchPopover');
    if (!search || !popover || !select) return;
    var sections = Array.prototype.slice.call(document.querySelectorAll('.category'));
    var cards = Array.prototype.slice.call(document.querySelectorAll('.card')).map(function (card) {
      var section = card.closest('.category');
      return {
        card: card,
        code: card.querySelector('.card-code').textContent.trim(),
        title: card.querySelector('.card-title').textContent.trim(),
        category: section.querySelector('.cat-heading').textContent.trim(),
        section: section
      };
    });

    function categoryKey(label) {
      return label.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');
    }

    function resetView() {
      cards.forEach(function (item) {
        item.card.classList.remove('is-hidden', 'is-selected');
      });
      sections.forEach(function (section) { section.classList.remove('is-hidden'); });
    }

    function hideResults() {
      if (results) {
        results.hidden = true;
        results.innerHTML = '';
      }
      close(popover);
    }

    function showAll() {
      resetView();
      hideResults();
    }

    function selectValue(value, shouldScroll) {
      search.value = '';
      select.value = value;
      resetView();
      hideResults();

      if (value === 'all') {
        showAll();
        return;
      }

      var parts = value.split(':');
      if (parts[0] === 'category') {
        var target = sections.filter(function (section) {
          return categoryKey(section.querySelector('.cat-heading').textContent) === parts[1];
        })[0];
        sections.forEach(function (section) {
          if (section !== target) section.classList.add('is-hidden');
        });
        if (target && shouldScroll) target.scrollIntoView({ behavior: 'smooth', block: 'start' });
        return;
      }

      var code = parts.slice(1).join(':');
      var card = cards.filter(function (item) { return item.code === code; })[0];
      cards.forEach(function (item) {
        if (item !== card) item.card.classList.add('is-hidden');
      });
      sections.forEach(function (section) {
        if (!card || section !== card.section) section.classList.add('is-hidden');
      });
      if (card) {
        card.card.classList.add('is-selected');
        if (shouldScroll) card.card.scrollIntoView({ behavior: 'smooth', block: 'center' });
      }
    }

    function runSearch() {
      var query = search.value.trim().toLowerCase();
      select.value = 'all';
      resetView();
      if (!query) {
        showAll();
        return;
      }

      var matches = cards.filter(function (item) {
        return (item.code + ' ' + item.title + ' ' + item.category).toLowerCase().indexOf(query) !== -1;
      });
      var matchingSections = {};
      matches.forEach(function (item) { matchingSections[sections.indexOf(item.section)] = item.section; });
      cards.forEach(function (item) {
        if (matches.indexOf(item) === -1) item.card.classList.add('is-hidden');
      });
      sections.forEach(function (section, index) {
        if (!matchingSections[index]) section.classList.add('is-hidden');
      });

      var noteHits = hits(query);
      if (results) {
        results.hidden = true;
        results.innerHTML = '';
      }
      if (!matches.length && !noteHits.length) {
        popover.hidden = false;
        popover.innerHTML = '<p class="result-empty">No matching standards. Try “IFRS 15” or “impairment”.</p>';
        return;
      }
      render(popover, noteHits, 0, query);
    }

    select.addEventListener('change', function () { selectValue(select.value, true); });
    search.addEventListener('input', runSearch);
    if (clearSearch) {
      clearSearch.addEventListener('click', function () {
        search.value = '';
        runSearch();
      });
    }
  }

  function mount() {
    mountChapter();
    mountHome();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', mount);
  } else {
    mount();
  }
}());
