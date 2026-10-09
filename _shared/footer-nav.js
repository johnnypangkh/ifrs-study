/* Prev/next footer from the pack page chain.
   chrome-packs.js is the shared list. PACK_PILLS still wins if a page sets it. */
(function () {
  function packChain() {
    if (window.PACK_PILLS && window.PACK_PILLS.length) return window.PACK_PILLS;
    var packs = window.CHROME_PACKS || {};
    var id = document.body && document.body.getAttribute("data-pack");
    if (!id || !packs[id]) {
      var path = location.pathname || "";
      var routes = window.CHROME_PACK_PATHS || [];
      for (var i = 0; i < routes.length; i++) {
        if (path.indexOf(routes[i][0]) !== -1) id = routes[i][1];
      }
    }
    var pack = id && packs[id];
    if (!pack) return [];
    var chain = [{ href: pack.map || "index.html", label: "Map" }];
    var chapters = pack.chapters || [];
    var meta = pack.meta || [];
    var n;
    for (n = 0; n < chapters.length; n++) chain.push(chapters[n]);
    for (n = 0; n < meta.length; n++) chain.push(meta[n]);
    return chain;
  }

  var PILLS = packChain();
  if (!PILLS || !PILLS.length) return;

  function currentFile() {
    var path = location.pathname || "";
    var file = path.split("/").pop() || "";
    file = file.split("?")[0].split("#")[0];
    if (!file || file.indexOf(".") === -1) return "index.html";
    return file;
  }

  function footerName(label) {
    return String(label).replace(/^\d+\s+/, "");
  }

  function mapPill() {
    for (var i = 0; i < PILLS.length; i++) {
      if (PILLS[i].href === "index.html") return PILLS[i];
    }
    return null;
  }

  function link(href, text, className) {
    var a = document.createElement("a");
    if (className) a.className = className;
    a.href = href;
    a.textContent = text;
    return a;
  }

  function mount(nav) {
    if (!nav || nav.getAttribute("data-footer-nav-ready") === "true") return;
    var file = currentFile();
    var index = -1;
    for (var i = 0; i < PILLS.length; i++) {
      if (PILLS[i].href === file) {
        index = i;
        break;
      }
    }
    if (index < 0) return;

    while (nav.firstChild) nav.removeChild(nav.firstChild);

    if (index > 0) {
      var prev = PILLS[index - 1];
      nav.appendChild(link(prev.href, "← Prev: " + footerName(prev.label)));
    } else {
      nav.appendChild(document.createElement("span"));
    }

    var map = mapPill();
    if (map && file !== map.href) {
      nav.appendChild(link(map.href, footerName(map.label), "mid"));
    }

    if (index < PILLS.length - 1) {
      var next = PILLS[index + 1];
      nav.appendChild(link(next.href, "Next: " + footerName(next.label) + " →"));
    } else {
      nav.appendChild(document.createElement("span"));
    }

    nav.setAttribute("data-footer-nav-ready", "true");
  }

  function boot() {
    var navs = document.querySelectorAll("nav.footer-nav");
    if (!navs.length) return false;
    for (var i = 0; i < navs.length; i++) mount(navs[i]);
    return true;
  }

  if (!boot() && document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot);
  }
})();
