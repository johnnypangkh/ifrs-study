/* CF draft theme — night-only. Always force data-theme=dark.
   Storage: force localStorage cf-draft-theme="dark" (migrates/clears any light|system|other). */
(function () {
  var KEY = "cf-draft-theme";
  var root = document.documentElement;

  function forceDark() {
    root.setAttribute("data-theme", "dark");
    try {
      localStorage.setItem(KEY, "dark");
    } catch (e) {}
  }

  forceDark();

  /* Idempotent: no .theme-toggle wiring (button removed from chrome). */
  window.cfDraftTheme = {
    apply: function () {
      forceDark();
    },
    toggle: function () {
      forceDark();
    },
    stored: function () {
      return "dark";
    },
    resolved: function () {
      return "dark";
    }
  };

  window.addEventListener("storage", function (e) {
    if (e.key === KEY) forceDark();
  });
})();

/* Embed: tell parent chapter the content height so iframe can auto-fit */
(function () {
  function notify() {
    if (!document.body || !document.body.classList.contains("embed")) return;
    var h = Math.max(
      document.body.scrollHeight || 0,
      document.body.offsetHeight || 0,
      document.documentElement ? document.documentElement.scrollHeight : 0,
      document.documentElement ? document.documentElement.offsetHeight : 0
    );
    try {
      if (window.parent && window.parent !== window) {
        window.parent.postMessage({ type: "cf-visual-height", height: h }, "*");
      }
    } catch (e) {}
  }

  if (!document.body || !document.body.classList.contains("embed")) return;

  function boot() {
    notify();
    requestAnimationFrame(notify);
    setTimeout(notify, 50);
    setTimeout(notify, 250);
    if (typeof ResizeObserver !== "undefined" && document.body) {
      new ResizeObserver(notify).observe(document.body);
    }
    window.addEventListener("load", notify);
    if (document.fonts && document.fonts.ready) {
      document.fonts.ready.then(notify).catch(function () {});
    }
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot);
  } else {
    boot();
  }
})();
