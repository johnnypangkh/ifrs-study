/* Shared chapter top bar. Loaded by chrome-include.js on every pack page.
   Title, pills, and the search placeholder come from chrome-packs.js.
   Desktop | Mobile is per pack in localStorage and only changes the
   Concept Map iframe width. Night theme stays in theme.js. */
(function () {
  var HINT = "Map width forced to 390px (iframe media queries follow). Teaching body unchanged.";
  var HOME = "../../homepage/homepage-wireframe-v0.1.html";

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

  function build(bar, pack, id) {
    if (bar.getAttribute("data-chrome") === "ready") return;
    var titleRow = document.createElement("div");
    titleRow.className = "chrome-bar-title chrome-row chrome-row-primary";

    var brand = document.createElement("div");
    brand.className = "chrome-brand";
    var line = document.createElement("div");
    line.className = "chrome-title-line";
    var label = document.createElement("p");
    label.className = "chrome-brand-label";
    label.textContent = pack.title;
    line.appendChild(label);

    var meta = document.createElement("div");
    meta.className = "chrome-brand-meta";
    var home = document.createElement("a");
    home.className = "chrome-home";
    home.href = HOME;
    home.textContent = "Home";
    var sep = document.createElement("span");
    sep.className = "chrome-meta-sep";
    sep.setAttribute("aria-hidden", "true");
    sep.textContent = "·";
    var last = document.createElement("span");
    last.className = "chrome-last-update";
    meta.appendChild(home);
    meta.appendChild(sep);
    meta.appendChild(last);
    brand.appendChild(line);
    brand.appendChild(meta);

    var actions = document.createElement("div");
    actions.className = "chrome-actions chrome-bar-actions";
    titleRow.appendChild(brand);
    titleRow.appendChild(actions);

    var nav = document.createElement("nav");
    nav.className = "tag-row-wrap";
    nav.setAttribute("aria-label", "Chapters");
    nav.setAttribute("data-pill-bar", "");
    var row = document.createElement("div");
    row.className = "tag-row";
    var file = currentFile();
    var pills = pack.pills || [];
    for (var i = 0; i < pills.length; i++) {
      var pill = pills[i];
      var link = document.createElement("a");
      var active = pill.href === file;
      link.className = active ? "tag active" : "tag";
      link.href = pill.href;
      link.textContent = pill.label;
      if (active) link.setAttribute("aria-current", "page");
      row.appendChild(link);
    }
    nav.appendChild(row);

    bar.replaceChildren(titleRow, nav);
    bar.classList.add("is-shared");
    bar.setAttribute("data-chrome", "ready");
    bar.setAttribute("data-chrome-pack", id);
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
    return true;
  }

  function mountMap(bar, id) {
    var iframe = document.querySelector(".visual-section iframe");
    var line = bar.querySelector(".chrome-title-line");
    if (!iframe || !line || line.querySelector(".view-switch")) return;
    var fieldset = iframe.closest(".visual-fieldset") || iframe.parentNode;
    var viewport = iframe.closest(".map-viewport");
    if (!viewport) {
      viewport = document.createElement("div");
      viewport.className = "map-viewport";
      iframe.parentNode.insertBefore(viewport, iframe);
      viewport.appendChild(iframe);
    }
    var hint = fieldset.querySelector(".view-switch-hint");
    if (!hint) {
      hint = document.createElement("p");
      hint.className = "view-switch-hint";
      hint.textContent = HINT;
      fieldset.insertBefore(hint, viewport);
    }
    var group = document.createElement("div");
    group.className = "view-switch";
    group.setAttribute("role", "group");
    group.setAttribute("aria-label", "Concept Map view width");
    ["desktop", "mobile"].forEach(function (mode) {
      var btn = document.createElement("button");
      btn.type = "button";
      btn.className = "view-switch-btn";
      btn.setAttribute("data-view", mode);
      btn.textContent = mode === "desktop" ? "Desktop" : "Mobile";
      group.appendChild(btn);
    });
    line.appendChild(group);

    function apply(mode, persist) {
      var name = mode === "mobile" ? "mobile" : "desktop";
      viewport.setAttribute("data-view", name);
      hint.classList.toggle("is-on", name === "mobile");
      var buttons = group.querySelectorAll(".view-switch-btn");
      for (var i = 0; i < buttons.length; i++) {
        var on = buttons[i].getAttribute("data-view") === name;
        buttons[i].setAttribute("aria-pressed", on ? "true" : "false");
      }
      if (persist) writeView(id, name);
      refit();
      tuneScroll(bar);
    }

    group.addEventListener("click", function (event) {
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
    mountMap(bar, id);
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
