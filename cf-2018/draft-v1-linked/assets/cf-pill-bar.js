/* CF 2018 chapter pill bar.
   Single source for every active page in draft-v1-linked.
   Pages mount an empty nav[data-cf-pill-bar]; this file fills it. */
(function () {
  var PILLS = [
    { href: "index.html", label: "Map" },
    { href: "ch01.html", label: "1 Objective & users" },
    { href: "ch02.html", label: "2 Qualitative" },
    { href: "ch03.html", label: "3 Reporting entity" },
    { href: "ch04.html", label: "4 Elements" },
    { href: "ch05.html", label: "5 Recognition" },
    { href: "ch06.html", label: "6 Measurement" },
    { href: "ch07.html", label: "7 Presentation" },
    { href: "ch08.html", label: "8 Capital" },
    { href: "ch09.html", label: "9 Combined FS" },
    { href: "ch10.html", label: "10 Carve-out" },
    { href: "ch11.html", label: "11 Status" },
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
    if (!nav || nav.getAttribute("data-cf-pill-bar-ready") === "true") return;
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
    nav.setAttribute("data-cf-pill-bar-ready", "true");
  }

  function boot() {
    var nodes = document.querySelectorAll("nav[data-cf-pill-bar]");
    if (!nodes.length) return false;
    for (var i = 0; i < nodes.length; i++) mount(nodes[i]);
    return true;
  }

  if (!boot() && document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot);
  }
})();
