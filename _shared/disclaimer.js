/* Pack disclaimer. Loaded by chrome-include.js on every pack page.
   The wording is the disclaimer field in chrome-packs.js.
   An empty aside#pack-disclaimer is filled from that field.
   If the aside is missing, it is inserted immediately before nav.footer-nav.
   chrome-1.css owns the box. This file sets no layout styles. */
(function () {
  function packId() {
    var packs = window.CHROME_PACKS || {};
    var body = document.body;
    var fromBody = body && body.getAttribute("data-pack");
    if (fromBody && packs[fromBody]) return fromBody;
    var path = location.pathname || "";
    var routes = window.CHROME_PACK_PATHS || [];
    var i;
    for (i = 0; i < routes.length; i++) {
      if (path.indexOf(routes[i][0]) !== -1) return routes[i][1];
    }
    return "";
  }

  function isEmpty(aside) {
    var text = aside.textContent || "";
    return text.replace(/\s/g, "") === "";
  }

  function boot() {
    if (!document.body) return;
    var id = packId();
    var pack = id && window.CHROME_PACKS ? window.CHROME_PACKS[id] : null;
    var html = pack && pack.disclaimer;
    if (!html) return;
    var aside = document.getElementById("pack-disclaimer");
    if (aside && aside.getAttribute("data-disclaimer-ready") === "true") return;
    if (!aside) {
      var nav = document.querySelector("nav.footer-nav");
      if (!nav || !nav.parentNode) return;
      aside = document.createElement("aside");
      aside.className = "callout pack-disclaimer";
      aside.id = "pack-disclaimer";
      nav.parentNode.insertBefore(aside, nav);
    }
    if (!isEmpty(aside)) return;
    aside.innerHTML = html;
    aside.setAttribute("data-disclaimer-ready", "true");
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", boot);
  else boot();
})();
