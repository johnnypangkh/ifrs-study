/* CF draft — auto-fit .visual-section iframes to content height.
   Prefer postMessage from embed theme.js (works on file:// when contentDocument
   is blocked). Same-origin contentDocument measure as fallback.
   Gate: iframe height fits content (no silent clip). Night-only unchanged. */
(function () {
  var MSG = "cf-visual-height";
  var PAD = 2; /* match theme.js embed notify buffer */
  /* Temporary floor only when measure stays 0 (e.g. blocked contentDocument
     before first postMessage). CSS also sets min-height; JS grows taller. */
  var FALLBACK_MIN = 260;

  function measure(iframe) {
    var h = 0;
    try {
      var doc = iframe.contentDocument;
      if (doc && doc.documentElement) {
        var body = doc.body;
        /* body only: <html> stretches to the iframe viewport (ratchet) */
        h = Math.max(
          body ? body.scrollHeight : 0,
          body ? Math.ceil(body.getBoundingClientRect().height) : 0
        );
      }
    } catch (e) {}
    if (h > 0) h += PAD;
    return h;
  }

  function applyHeight(iframe, h) {
    if (!h || h < 1) return;
    iframe.style.height = Math.ceil(h) + "px";
    /* allow CSS min-height floor until we have a real fit; then clear override */
    iframe.style.minHeight = "";
    iframe.removeAttribute("scrolling");
    iframe.setAttribute("scrolling", "no");
  }

  function fit(iframe) {
    var h = measure(iframe);
    if (h > 0) {
      applyHeight(iframe, h);
      return;
    }
    /* measure 0: do not leave browser default ~150px — retry, then temp floor */
    requestAnimationFrame(function () {
      var h2 = measure(iframe);
      if (h2 > 0) {
        applyHeight(iframe, h2);
        return;
      }
      setTimeout(function () {
        var h3 = measure(iframe);
        if (h3 > 0) {
          applyHeight(iframe, h3);
        } else if (!iframe.style.height || parseInt(iframe.style.height, 10) < FALLBACK_MIN) {
          /* still 0 (likely file:// blocked contentDocument); hold floor until postMessage */
          iframe.style.minHeight = FALLBACK_MIN + "px";
          if (!iframe.style.height) iframe.style.height = FALLBACK_MIN + "px";
        }
      }, 100);
    });
  }

  function wire(iframe) {
    function run() {
      fit(iframe);
      /* second pass after layout/fonts */
      requestAnimationFrame(function () {
        fit(iframe);
        setTimeout(function () { fit(iframe); }, 50);
        setTimeout(function () { fit(iframe); }, 250);
        setTimeout(function () { fit(iframe); }, 600);
      });
    }

    iframe.addEventListener("load", function () {
      run();
      try {
        var doc = iframe.contentDocument;
        if (!doc || !doc.body) return;
        if (typeof ResizeObserver !== "undefined") {
          var ro = new ResizeObserver(function () { fit(iframe); });
          ro.observe(doc.body);
          if (doc.documentElement) ro.observe(doc.documentElement);
        }
        if (doc.fonts && doc.fonts.ready) {
          doc.fonts.ready.then(function () { fit(iframe); }).catch(function () {});
        }
        Array.prototype.forEach.call(doc.images || [], function (img) {
          if (!img.complete) img.addEventListener("load", function () { fit(iframe); });
        });
      } catch (e) {}
    });

    /* cached / already complete */
    try {
      if (iframe.contentDocument && iframe.contentDocument.readyState === "complete") {
        run();
      }
    } catch (e) {}
  }

  function init() {
    document.querySelectorAll(".visual-section iframe").forEach(wire);
  }

  /* Prefer postMessage height when received (file:// + http). */
  window.addEventListener("message", function (e) {
    var data = e && e.data;
    if (!data || data.type !== MSG || typeof data.height !== "number") return;
    var frames = document.querySelectorAll(".visual-section iframe");
    for (var i = 0; i < frames.length; i++) {
      if (frames[i].contentWindow === e.source) {
        applyHeight(frames[i], Math.ceil(data.height));
        break;
      }
    }
  });

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }

  window.addEventListener("resize", function () {
    document.querySelectorAll(".visual-section iframe").forEach(fit);
  });

  window.cfIframeFit = { fitAll: function () {
    document.querySelectorAll(".visual-section iframe").forEach(fit);
  }};
})();
