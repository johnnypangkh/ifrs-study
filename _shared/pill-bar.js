/* Shared chapter pill bar.
   Each pack page loads its own pill list first, which sets window.PACK_PILLS.
   Pages mount an empty nav[data-ias2-pill-bar], nav[data-ifrs18-pill-bar],
   or nav[data-cf-pill-bar]; this file fills it. */
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

  function readyName(nav) {
    if (nav.hasAttribute("data-ias2-pill-bar")) return "data-ias2-pill-bar-ready";
    if (nav.hasAttribute("data-ifrs18-pill-bar")) return "data-ifrs18-pill-bar-ready";
    if (nav.hasAttribute("data-cf-pill-bar")) return "data-cf-pill-bar-ready";
    return "data-pill-bar-ready";
  }

  function mount(nav) {
    var ready = readyName(nav);
    if (!nav || nav.getAttribute(ready) === "true") return;
    var file = currentFile();
    var row = document.createElement("div");
    row.className = "tag-row";
    for (var i = 0; i < PILLS.length; i++) {
      var pill = PILLS[i];
      var link = document.createElement("a");
      var active = pill.href === file;
      link.className = active ? "tag active" : "tag";
      link.href = pill.href;
      link.textContent = pill.label;
      if (active) link.setAttribute("aria-current", "page");
      row.appendChild(link);
    }
    while (nav.firstChild) nav.removeChild(nav.firstChild);
    nav.appendChild(row);
    nav.setAttribute(ready, "true");
  }

  function boot() {
    var nodes = document.querySelectorAll(
      "nav[data-ias2-pill-bar], nav[data-ifrs18-pill-bar], nav[data-cf-pill-bar]"
    );
    if (!nodes.length) return false;
    for (var i = 0; i < nodes.length; i++) mount(nodes[i]);
    return true;
  }

  if (!boot() && document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot);
  }
})();
