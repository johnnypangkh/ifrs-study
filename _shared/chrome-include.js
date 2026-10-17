/* One chrome include for every draft page.
   Writes the shared chrome styles, theme, iframe fit, search index, and search.
   Pack pages load this file instead of pasting those tags.
   INDEX is the search-index.js stamp. build-search-index.py rewrites it.
   Map values are sha256[:12]. stamp-assets.py rewrites them. */
(function () {
  var V = {
    "chrome.css": "85d3da921d08",
    "theme.js": "a1d54e6efe0c",
    "iframe-fit.js": "afb82ab9f5ec",
    "chrome-packs.js": "e57789e94f9f",
    "disclaimer.js": "a7c477196e77",
    "chrome-bar.js": "1f0dd2c5251c",
    "search.js": "85ee050b8575"
  };
  var INDEX = "04ac0c0d58be";
  var src = (document.currentScript && document.currentScript.src) || "";
  var dir = src.replace(/[^/?]*(\?.*)?$/, "");
  if (!dir) dir = "../../_shared/";

  function asset(file) {
    return dir + file + "?v=" + V[file];
  }

  var root = dir.replace(/_shared\/$/, "");
  document.write('<link rel="stylesheet" href="' + asset("chrome.css") + '">');
  document.write('<script src="' + asset("theme.js") + '"><\/script>');
  document.write('<script src="' + asset("iframe-fit.js") + '"><\/script>');
  document.write('<script src="' + root + 'homepage/search-index.js?v=' + INDEX + '"><\/script>');
  document.write('<script src="' + asset("chrome-packs.js") + '"><\/script>');
  document.write('<script src="' + asset("disclaimer.js") + '"><\/script>');
  document.write('<script src="' + asset("chrome-bar.js") + '"><\/script>');
  document.write('<script src="' + asset("search.js") + '"><\/script>');
})();
