/* Prev/next footer from the pack pill list.
   window.PACK_PILLS is the only page chain. Loaded after that list. */
(function () {
  var PILLS = window.PACK_PILLS;
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
