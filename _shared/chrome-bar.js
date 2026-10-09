/* Shared chapter top bar. Loaded by chrome-include.js on every pack page.
   Title, pills, and the search placeholder come from chrome-packs.js.
   Option B: Home / pack title (links to the pack Map), Desktop|Mobile
   beside the title on every page, search with the clear control inside,
   chapter pills only. Abbreviations and References sit under the H1.
   The switch slot is always the same size. Without a map iframe it
   does not change layout and does not scroll a map.
   Pill chevrons scroll the row to the end so the last pill clears the fade. */
(function () {
  var HINT = "Mobile preview";
  var HOME = "../../homepage/homepage-wireframe-v0.1.html";
  var GLASS = '<svg viewBox="0 0 16 16" aria-hidden="true"><circle cx="7" cy="7" r="4.5"></circle><path d="M10.5 10.5l3.5 3.5"></path></svg>';
  var ICON = {
    desktop: '<svg viewBox="0 0 16 16" aria-hidden="true"><rect x="1.5" y="2.5" width="13" height="8.5" rx="1"></rect><path d="M5.5 13.5h5M8 11v2.5"></path></svg>',
    mobile: '<svg viewBox="0 0 16 16" aria-hidden="true"><rect x="4.5" y="1.5" width="7" height="13" rx="1.4"></rect><path d="M7 12.3h2"></path></svg>'
  };

  function packId() {
    var packs = window.CHROME_PACKS || {};
    var body = document.body;
    var fromBody = body && body.getAttribute("data-pack");
    if (fromBody && packs[fromBody]) return fromBody;
    var path = location.pathname || "";
    var routes = window.CHROME_PACK_PATHS || [];
    for (var i = 0; i < routes.length; i++) {
      if (path.indexOf(routes[i][0]) !== -1) return routes[i][1];
    }
    return "";
  }

  function currentFile() {
    var file = (location.pathname || "").split("/").pop() || "";
    file = file.split("?")[0].split("#")[0];
    if (!file || file.indexOf(".") === -1) return "index.html";
    return file;
  }

  function storageKey(id) {
    return "chrome-map-view:" + id;
  }

  function readView(id) {
    try {
      var stored = localStorage.getItem(storageKey(id));
      if (stored === "mobile" || stored === "desktop") return stored;
    } catch (err) {}
    return "desktop";
  }

  function writeView(id, mode) {
    try { localStorage.setItem(storageKey(id), mode); } catch (err) {}
  }

  function chevron(dir) {
    var btn = document.createElement("button");
    btn.type = "button";
    btn.className = "pill-chevron pill-chevron-" + dir;
    btn.setAttribute("aria-label", dir === "next" ? "Show later chapters" : "Show earlier chapters");
    btn.hidden = true;
    var svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
    svg.setAttribute("viewBox", "0 0 16 16");
    svg.setAttribute("aria-hidden", "true");
    var path = document.createElementNS("http://www.w3.org/2000/svg", "path");
    path.setAttribute("d", dir === "next" ? "M6 3.5l4.5 4.5L6 12.5" : "M10 3.5L5.5 8 10 12.5");
    svg.appendChild(path);
    btn.appendChild(svg);
    return btn;
  }

  function build(bar, pack, id) {
    if (bar.getAttribute("data-chrome") === "ready") return;
    var file = currentFile();
    var inner = document.createElement("div");
    inner.className = "chrome-inner";

    var row = document.createElement("div");
    row.className = "chrome-row1";

    var idn = document.createElement("div");
    idn.className = "chrome-idn";
    var home = document.createElement("a");
    home.className = "chrome-home";
    home.href = HOME;
    home.setAttribute("aria-label", "Home");
    home.innerHTML = '<span class="chrome-home-mark" aria-hidden="true">←</span><span class="chrome-home-txt">Home</span><span class="chrome-home-sep" aria-hidden="true">/</span>';
    var title = document.createElement("a");
    title.className = "chrome-brand-label";
    title.href = pack.map || "index.html";
    title.textContent = pack.title;
    title.title = pack.title;
    idn.appendChild(home);
    idn.appendChild(title);

    var search = document.createElement("label");
    search.className = "chapter-search";
    search.innerHTML =
      '<svg class="chapter-search-glass" viewBox="0 0 16 16" aria-hidden="true"><circle cx="7" cy="7" r="4.5"></circle><path d="M10.5 10.5l3.5 3.5"></path></svg>' +
      '<input class="chapter-search-input" id="chapterSearch" type="search" autocomplete="off" enterkeyhint="search" placeholder="" aria-label="' + pack.search.replace(/"/g, "") + '" />' +
      '<button class="chapter-search-clear" id="chapterSearchClear" type="button" aria-label="Clear search">✕</button>' +
      '<div class="search-popover" id="chapterSearchPopover" hidden></div>';

    var open = document.createElement("button");
    open.type = "button";
    open.className = "chapter-search-open";
    open.setAttribute("aria-label", "Search");
    open.innerHTML = GLASS;

    row.appendChild(idn);
    row.appendChild(search);
    row.appendChild(open);

    var nav = document.createElement("nav");
    nav.className = "pill-bar";
    nav.setAttribute("aria-label", "Chapters");
    var scroller = document.createElement("div");
    scroller.className = "tag-row-wrap";
    scroller.setAttribute("data-pill-bar", "");
    var pills = document.createElement("div");
    pills.className = "tag-row";
    var chapters = pack.chapters || [];
    for (var i = 0; i < chapters.length; i++) {
      var pill = chapters[i];
      var link = document.createElement("a");
      var active = pill.href === file;
      link.className = active ? "tag active" : "tag";
      link.href = pill.href;
      link.textContent = pill.label;
      if (active) link.setAttribute("aria-current", "page");
      pills.appendChild(link);
    }
    scroller.appendChild(pills);
    var prev = chevron("prev");
    var next = chevron("next");
    nav.appendChild(scroller);
    nav.appendChild(prev);
    nav.appendChild(next);

    inner.appendChild(row);
    inner.appendChild(nav);
    bar.replaceChildren(inner);
    bar.classList.add("is-shared");
    bar.setAttribute("data-chrome", "ready");
    bar.setAttribute("data-chrome-pack", id);
    mountMeta(pack, file);
    wireSearch(bar, search, open);
    wirePills(nav, scroller, prev, next);
  }

  function mountMeta(pack, file) {
    if (document.querySelector(".chrome-page-meta")) return;
    var header = document.querySelector(".page-header") || document.querySelector("main");
    var h1 = (header && header.querySelector("h1")) || document.querySelector("h1");
    if (!h1) return;
    var line = document.createElement("p");
    line.className = "chrome-page-meta";
    var last = document.createElement("span");
    last.className = "chrome-last-update";
    line.appendChild(last);
    var links = pack.meta || [];
    for (var i = 0; i < links.length; i++) {
      var sep = document.createElement("span");
      sep.className = "chrome-meta-sep";
      sep.setAttribute("aria-hidden", "true");
      sep.textContent = "·";
      var a = document.createElement("a");
      a.href = links[i].href;
      a.textContent = links[i].label;
      if (links[i].href === file) a.setAttribute("aria-current", "page");
      line.appendChild(sep);
      line.appendChild(a);
    }
    h1.insertAdjacentElement("afterend", line);
  }

  function wireSearch(bar, search, open) {
    var input = search.querySelector("input");
    open.addEventListener("click", function () {
      bar.classList.add("is-searching");
      if (input) input.focus();
    });
    if (!input) return;
    input.addEventListener("blur", function () {
      if (!input.value) bar.classList.remove("is-searching");
    });
  }

  function maxScroll(scroller) {
    return Math.max(0, scroller.scrollWidth - scroller.clientWidth);
  }

  function wirePills(nav, scroller, prev, next) {
    var lock = false;
    function tune(resize) {
      if (lock) return;
      if (resize || !nav.classList.contains("is-overflowing")) {
        lock = true;
        var wasEnd = false;
        if (resize && nav.classList.contains("is-overflowing")) {
          var before = maxScroll(scroller);
          wasEnd = before <= 1 || scroller.scrollLeft >= before - 1;
          nav.classList.remove("is-overflowing");
        }
        var overflows = scroller.scrollWidth - scroller.clientWidth > 1;
        nav.classList.toggle("is-overflowing", overflows);
        if (wasEnd) scroller.scrollLeft = maxScroll(scroller);
        lock = false;
      }
      var max = maxScroll(scroller);
      var left = scroller.scrollLeft;
      var live = max > 1;
      next.hidden = !live || left >= max - 1;
      prev.hidden = !live || left <= 1;
    }
    function sync() { tune(false); }

    function step(dir) {
      var max = maxScroll(scroller);
      var fade = next.offsetWidth || 40;
      var page = Math.max(fade + 16, scroller.clientWidth - fade);
      var target = scroller.scrollLeft + dir * page;
      if (dir > 0) target = Math.min(max, target);
      else target = Math.max(0, target);
      if (dir > 0 && max - target < 2) target = max;
      if (dir < 0 && target < 2) target = 0;
      var reduce = false;
      try { reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches; } catch (err) {}
      scroller.scrollTo({ left: target, behavior: reduce ? "auto" : "smooth" });
    }

    next.addEventListener("click", function () { step(1); });
    prev.addEventListener("click", function () { step(-1); });
    scroller.addEventListener("scroll", sync, { passive: true });
    window.addEventListener("resize", function () { tune(true); });
    if (typeof ResizeObserver !== "undefined") {
      new ResizeObserver(function () { tune(true); }).observe(scroller);
    }
    tune(true);
    revealCurrent(scroller);
    tune(false);
  }

  function revealCurrent(scroller) {
    var current = scroller.querySelector('[aria-current="page"]');
    if (!current) return;
    var host = scroller.getBoundingClientRect();
    var pill = current.getBoundingClientRect();
    var fade = 44;
    if (pill.right > host.right - fade) scroller.scrollLeft += pill.right - (host.right - fade);
    if (pill.left < host.left + 4) scroller.scrollLeft -= (host.left + 4) - pill.left;
    var max = maxScroll(scroller);
    if (scroller.scrollLeft > max) scroller.scrollLeft = max;
  }

  function refit() {
    var api = window.cfIframeFit;
    if (!api || typeof api.fitAll !== "function") return;
    api.fitAll();
    requestAnimationFrame(function () {
      api.fitAll();
      setTimeout(api.fitAll, 50);
      setTimeout(api.fitAll, 250);
      setTimeout(api.fitAll, 600);
    });
  }

  function tuneScroll(bar) {
    var height = Math.ceil(bar.getBoundingClientRect().height);
    if (height < 1) return;
    document.documentElement.style.setProperty("--chrome-sticky-offset", (height + 16) + "px");
  }

  function markSearch(pack) {
    var input = document.getElementById("chapterSearch");
    if (!input || !pack) return false;
    input.setAttribute("placeholder", pack.search);
    input.setAttribute("aria-label", pack.search);
    return true;
  }

  function mountSwitch(bar, id) {
    var row = bar.querySelector(".chrome-row1");
    var idn = bar.querySelector(".chrome-idn");
    if (!row || !idn || row.querySelector(".view-switch")) return;
    var iframe = document.querySelector(".visual-section iframe");
    var hasMap = !!iframe;
    var viewport = null;
    var hint = null;
    if (hasMap) {
      var fieldset = iframe.closest(".visual-fieldset") || iframe.parentNode;
      viewport = iframe.closest(".map-viewport");
      if (!viewport) {
        viewport = document.createElement("div");
        viewport.className = "map-viewport";
        iframe.parentNode.insertBefore(viewport, iframe);
        viewport.appendChild(iframe);
      }
      hint = fieldset.querySelector(".view-switch-hint");
      if (!hint) {
        hint = document.createElement("p");
        hint.className = "view-switch-hint";
        hint.textContent = HINT;
        fieldset.insertBefore(hint, viewport);
      }
    }

    var group = document.createElement("div");
    group.className = "view-switch";
    group.setAttribute("role", "group");
    group.setAttribute("aria-label", "Concept Map view width");
    if (!hasMap) group.setAttribute("data-map", "off");
    ["desktop", "mobile"].forEach(function (mode) {
      var btn = document.createElement("button");
      btn.type = "button";
      btn.className = "view-switch-btn";
      btn.setAttribute("data-view", mode);
      btn.innerHTML = ICON[mode] + '<span class="txt">' + (mode === "desktop" ? "Desktop" : "Mobile") + "</span>";
      if (!hasMap) btn.setAttribute("aria-disabled", "true");
      group.appendChild(btn);
    });
    idn.insertAdjacentElement("afterend", group);

    function apply(mode, persist) {
      var name = mode === "mobile" ? "mobile" : "desktop";
      if (viewport) viewport.setAttribute("data-view", name);
      if (hint) hint.classList.toggle("is-on", hasMap && name === "mobile");
      var buttons = group.querySelectorAll(".view-switch-btn");
      for (var i = 0; i < buttons.length; i++) {
        var on = buttons[i].getAttribute("data-view") === name;
        buttons[i].setAttribute("aria-pressed", on ? "true" : "false");
      }
      if (persist && hasMap) writeView(id, name);
      if (hasMap) refit();
      tuneScroll(bar);
    }

    group.addEventListener("click", function (event) {
      if (!hasMap) return;
      var btn = event.target.closest(".view-switch-btn");
      if (!btn || !group.contains(btn)) return;
      apply(btn.getAttribute("data-view"), true);
    });
    apply(readView(id), false);
  }

  function boot() {
    if (!document.body) return;
    var id = packId();
    var pack = id && window.CHROME_PACKS ? window.CHROME_PACKS[id] : null;
    if (!pack) return;
    if (!document.body.getAttribute("data-pack")) document.body.setAttribute("data-pack", id);
    var bar = document.querySelector("header.chrome-bar");
    if (!bar) {
      bar = document.createElement("header");
      bar.className = "chrome-bar";
      document.body.insertBefore(bar, document.body.firstChild);
    }
    build(bar, pack, id);
    mountSwitch(bar, id);
    tuneScroll(bar);
    if (!markSearch(pack)) {
      requestAnimationFrame(function () { markSearch(pack); });
      setTimeout(function () { markSearch(pack); }, 0);
    }
    if (typeof ResizeObserver !== "undefined") {
      new ResizeObserver(function () { tuneScroll(bar); }).observe(bar);
    }
    window.addEventListener("resize", function () { tuneScroll(bar); });
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", boot);
  else boot();
})();
