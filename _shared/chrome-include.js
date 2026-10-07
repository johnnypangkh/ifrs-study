/* One chrome include for every draft page.
   Writes the shared chrome styles, theme, iframe fit, search index, and search.
   Pack pages load this file instead of pasting those tags.
   INDEX is the search-index.js stamp. build-search-index.py rewrites it. */
(function () {
  var V = "chrome-row-20261006";
  var INDEX = "1420f41616a1";
  var src = (document.currentScript && document.currentScript.src) || "";
  var dir = src.replace(/[^/?]*(\?.*)?$/, "");
  if (!dir) dir = "../../_shared/";

  function asset(file) {
    return dir + file + "?v=" + V;
  }

  var root = dir.replace(/_shared\/$/, "");
  document.write('<link rel="stylesheet" href="' + asset("chrome.css") + '">');
  document.write('<script src="' + asset("theme.js") + '"><\/script>');
  document.write('<script src="' + asset("iframe-fit.js") + '"><\/script>');
  document.write('<script src="' + root + 'homepage/search-index.js?v=' + INDEX + '"><\/script>');
  document.write('<script src="' + asset("search.js") + '"><\/script>');
})();
