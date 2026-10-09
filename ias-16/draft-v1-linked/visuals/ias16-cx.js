/* Shared connector engine for the IAS 16 chapter maps.
   Helpers match the master map's inline script. Master keeps that copy. */
(function (global) {
  function naturalHeight(cell) {
    var kids = [];
    var all = cell.children;
    for (var i = 0; i < all.length; i++) {
      if (getComputedStyle(all[i]).display === "none") continue;
      kids.push(all[i]);
    }
    var cs = getComputedStyle(cell);
    var extra = parseFloat(cs.paddingTop) + parseFloat(cs.paddingBottom)
      + parseFloat(cs.borderTopWidth) + parseFloat(cs.borderBottomWidth);
    if (!kids.length) return cell.getBoundingClientRect().height;
    var top = kids[0].getBoundingClientRect().top;
    var bot = kids[kids.length - 1].getBoundingClientRect().bottom;
    return (bot - top) + extra;
  }

  function equalise(root) {
    var groups = root.querySelectorAll("[data-eq]");
    var pending = [];
    for (var g = 0; g < groups.length; g++) {
      var cells = [];
      var kids = groups[g].children;
      for (var c = 0; c < kids.length; c++) {
        if (kids[c].hasAttribute("data-eq-cell")) cells.push(kids[c]);
      }
      if (cells.length < 2) continue;
      var row = groups[g].hasAttribute("data-eq-stack");
      if (!row) {
        var a0 = cells[0].getBoundingClientRect();
        row = true;
        for (var k = 1; k < cells.length; k++) {
          var bk = cells[k].getBoundingClientRect();
          if (Math.min(a0.bottom, bk.bottom) - Math.max(a0.top, bk.top) < 4) row = false;
        }
      }
      for (var j = 0; j < cells.length; j++) cells[j].style.minHeight = "0px";
      if (!row) continue;
      pending.push(cells);
    }
    if (!pending.length) return;
    void root.offsetHeight;
    for (var p = 0; p < pending.length; p++) {
      var cells = pending[p];
      var max = 0;
      for (var j = 0; j < cells.length; j++) {
        var h = naturalHeight(cells[j]);
        if (h > max) max = h;
      }
      if (!(max > 0)) continue;
      for (var j = 0; j < cells.length; j++) {
        var prev = parseFloat(cells[j].style.minHeight);
        if (Math.abs(prev - max) < 0.5) continue;
        cells[j].style.minHeight = max + "px";
      }
    }
  }

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
    }
  }

  function mount(root, spec) {
    if (!root) return;
    var layer = root.querySelector(".cx-layer");

    function em(n) {
      return n * (parseFloat(getComputedStyle(root).fontSize) || 13);
    }

    function boxOf(el) {
      var host = root.getBoundingClientRect();
      var b = el.getBoundingClientRect();
      return {
        l: b.left - host.left,
        t: b.top - host.top,
        r: b.right - host.left,
        b: b.bottom - host.top,
        cx: (b.left + b.right) / 2 - host.left,
        cy: (b.top + b.bottom) / 2 - host.top
      };
    }

    function shown(el) {
      return !!el && getComputedStyle(el).display !== "none" && el.getClientRects().length > 0;
    }

    function placeLabel(el, x, y, mode) {
      if (!el) return;
      var top = y + "px";
      var left = x + "px";
      var transform = mode === "above" ? "translate(-50%, -115%)"
        : mode === "left" ? "translate(-100%, -50%)"
        : "translateY(-50%)";
      if (el.style.left !== left) el.style.left = left;
      if (el.style.top !== top) el.style.top = top;
      if (el.style.transform !== transform) el.style.transform = transform;
    }

    function draw() {
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
      }
      function hFlow(y, x1, x2, lab, tone) {
        if (x2 - x1 < 8) return;
        h(y, x1, x2, tone || "");
        placeLabel(lab, (x1 + x2) / 2, y, "above");
      }
      function linkStem(src, tab) {
        if (!shown(src) || !shown(tab)) return;
        var A = boxOf(src);
        var B = boxOf(tab);
        var gap = B.t - A.b;
        if (gap < 16) return;
        if (Math.abs(A.cx - B.cx) <= 3) {
          v(A.cx, A.b, B.t, true);
          return;
        }
        var mid = A.b + gap * 0.5;
        v(A.cx, A.b, mid, true);
        h(mid, A.cx, B.cx, "link");
        v(B.cx, mid, B.t, true);
      }
      spec({
        root: root,
        narrow: narrow,
        em: em,
        boxOf: boxOf,
        shown: shown,
        placeLabel: placeLabel,
        v: v,
        h: h,
        vFlow: vFlow,
        hFlow: hFlow,
        linkStem: linkStem
      });
      while (layer.children.length < specs.length) layer.appendChild(document.createElement("span"));
      for (var i = 0; i < layer.children.length; i++) {
        var node = layer.children[i];
        if (i >= specs.length) {
          if (node.getAttribute("data-on") !== "0") {
            node.setAttribute("data-on", "0");
            node.style.display = "none";
          }
          continue;
        }
        var sp = specs[i];
        node.setAttribute("data-on", "1");
        node.className = sp.k;
        node.style.display = "block";
        node.style.left = sp.x + "px";
        node.style.top = sp.y + "px";
        if (sp.k.indexOf("v") === 0) {
          node.style.height = sp.h + "px";
          node.style.width = "";
        } else {
          node.style.width = sp.w + "px";
          node.style.height = "";
        }
      }
    }

    function fit() {
      equalise(root);
      alignLedgers(root);
      equalise(root);
      draw();
    }

    fit();
    window.addEventListener("resize", fit);
    if (window.ResizeObserver) new ResizeObserver(fit).observe(root);
    if (document.fonts && document.fonts.ready) {
      document.fonts.ready.then(fit).catch(function () {});
    }
  }

  global.Ias16Cx = { mount: mount };
})(window);
