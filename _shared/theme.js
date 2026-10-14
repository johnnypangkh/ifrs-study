/* Theme: follows prefers-color-scheme via tokens.css; nothing forced here (THEME row #74). */

/* Embed: tell parent chapter the content height so iframe can auto-fit.
   Script is in <head>, so body may be null at parse time — defer embed check
   until DOM ready. postMessage works on file:// when contentDocument does not. */
(function () {
  var PAD = 2; /* sub-pixel rounding buffer; fieldset padding gives the visual margin */

  function notify() {
    if (!document.body || !document.body.classList.contains("embed")) return;
    /* body only: <html> stretches to the iframe viewport, so measuring it
       makes the iframe ratchet taller on every notify and never shrink */
    var h = Math.max(
      document.body.scrollHeight || 0,
      Math.ceil(document.body.getBoundingClientRect().height) || 0
    );
    if (h > 0) h += PAD;
    try {
      if (window.parent && window.parent !== window) {
        window.parent.postMessage({ type: "cf-visual-height", height: h }, "*");
      }
    } catch (e) {}
  }

  function boot() {
    if (!document.body || !document.body.classList.contains("embed")) return;
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
