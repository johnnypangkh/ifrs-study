/* One chrome include for every draft page.
   Writes chrome.css, theme.js, and iframe-fit.js with the same cache query.
   Pages load this file instead of pasting those three lines. */
(function () {
  var V = "chrome-include-20261004";
  var src = (document.currentScript && document.currentScript.src) || "";
  var dir = src.replace(/[^/?]*(\?.*)?$/, "");
  if (!dir) dir = "../../_shared/";

  function asset(file) {
    return dir + file + "?v=" + V;
  }

  document.write('<link rel="stylesheet" href="' + asset("chrome.css") + '">');
  document.write('<script src="' + asset("theme.js") + '"><\/script>');
  document.write('<script src="' + asset("iframe-fit.js") + '"><\/script>');
})();
