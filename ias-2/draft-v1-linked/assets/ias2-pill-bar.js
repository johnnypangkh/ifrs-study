/* IAS 2 chapter pill bar.
   Single source for every active page in draft-v1-linked.
   Pages mount an empty nav[data-ias2-pill-bar]; this file fills it. */
(function () {
  var PILLS = [
    { href: "index.html", label: "Map" },
    { href: "abbreviations.html", label: "Abbreviations" },
    { href: "ch01.html", label: "1 Scope" },
    { href: "ch02.html", label: "2 Recognition" },
    { href: "ch03.html", label: "3 Initial measurement" },
    { href: "ch04.html", label: "4 Subsequent" },
    { href: "ch05.html", label: "5 Derecognition" },
    { href: "ch06.html", label: "6 Disclosure" },
    { href: "references.html", label: "References" }
  ];

  function currentFile() {
    var path = location.pathname || "";
    var file = path.split("/").pop() || "";
    file = file.split("?")[0].split("#")[0];
    if (!file || file.indexOf(".") === -1) return "index.html";
    return file;
  }

  function mount(nav) {
    if (!nav || nav.getAttribute("data-ias2-pill-bar-ready") === "true") return;
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
    nav.setAttribute("data-ias2-pill-bar-ready", "true");
  }

  function boot() {
    var nodes = document.querySelectorAll("nav[data-ias2-pill-bar]");
    if (!nodes.length) return false;
    for (var i = 0; i < nodes.length; i++) mount(nodes[i]);
    return true;
  }

  if (!boot() && document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot);
  }
})();
