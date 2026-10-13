/* SOURCE ias-16/draft-v1-linked/visuals/ias16-cx.js:65 @ cfc59d2b */
  function alignLedgers(root) {
    var leds = root.querySelectorAll(".carry-row .vledger");
    var terms = [];
    for (var i = 0; i < leds.length; i++) terms.push(leds[i].querySelectorAll(".vterm, .vresult"));
    var narrow = window.matchMedia("(max-width: 800px)").matches;
    for (var g = 0; g < terms.length; g++) {
      for (var j = 0; j < terms[g].length; j++) terms[g][j].style.minHeight = "0px";
    }
    if (narrow || terms.length < 2) return;
    void root.offsetHeight;
    var n = Math.min(terms[0].length, terms[1].length);
    for (var k = 0; k < n; k++) {
      var h = Math.max(terms[0][k].getBoundingClientRect().height, terms[1][k].getBoundingClientRect().height);
      if (!(h > 0)) continue;
      terms[0][k].style.minHeight = h + "px";
      terms[1][k].style.minHeight = h + "px";

/* SOURCE ias-16/draft-v1-linked/visuals/ias16-cx.js:119 @ cfc59d2b */
      if (!layer) return;
      var narrow = window.matchMedia("(max-width: 800px)").matches;
      var specs = [];
      function v(x, y1, y2, link) {
        if (!(y2 > y1 + 0.5)) return;
        specs.push({ k: link ? "v link" : "v", x: x, y: y1, h: y2 - y1 });
      }
      function h(y, x1, x2, tone) {
        if (x2 < x1) { var swap = x1; x1 = x2; x2 = swap; }
        if (!(x2 > x1 + 0.5)) return;
        specs.push({ k: tone ? "h " + tone : "h", x: x1, y: y, w: x2 - x1 });
      }
      function vFlow(x, y1, y2, lab) {
        if (y2 - y1 < 8) return;
        v(x, y1, y2, false);
        if (narrow) placeLabel(lab, x - em(0.55), (y1 + y2) / 2, "left");
        else placeLabel(lab, x + em(0.55), (y1 + y2) / 2, "right");

