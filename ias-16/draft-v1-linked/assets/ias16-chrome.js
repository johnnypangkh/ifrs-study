/* IAS 16 chapter chrome opt-in.
   Reshapes the sticky bar and, where a Concept Map iframe exists, mounts
   Desktop | Mobile. Widths live in assets/draft.css. Other packs do not
   load this file. */
(function () {
  var KEY = "ias16-map-view";
  var HINT = "Map width forced to 390px (iframe media queries follow). Teaching body unchanged.";

  function packTitle(cluster) {
    var fallback = "IAS 16 · Property, Plant and Equipment";
    if (!cluster) return fallback;
    var named = cluster.querySelector("span:not(.chrome-last-update)");
    var text = (named ? named.textContent : cluster.textContent).replace(/\s+/g, " ").trim();
    if (/^IAS\s*16\b/i.test(text)) return fallback;
    return text || fallback;
  }

  function reshape(bar) {
    var titleRow = bar.querySelector(".chrome-bar-title");
    if (!titleRow || titleRow.getAttribute("data-ias16-chrome") === "ready") return;
    var home = titleRow.querySelector("a.chrome-home");
    var cluster = titleRow.querySelector(".chrome-title-cluster");
    var last = titleRow.querySelector("span.chrome-last-update");
    var search = titleRow.querySelector(".chapter-search");

    var brand = document.createElement("div");
    brand.className = "chrome-brand";
    var label = document.createElement("p");
    label.className = "chrome-brand-label";
    label.textContent = packTitle(cluster);
    var meta = document.createElement("div");
    meta.className = "chrome-brand-meta";
    if (home) meta.appendChild(home);
    var sep = document.createElement("span");
    sep.className = "chrome-meta-sep";
    sep.setAttribute("aria-hidden", "true");
    sep.textContent = "·";
    meta.appendChild(sep);
    if (!last) {
      last = document.createElement("span");
      last.className = "chrome-last-update";
    }
    meta.appendChild(last);
    brand.appendChild(label);
    brand.appendChild(meta);

    var actions = titleRow.querySelector(".chrome-actions");
    if (!actions) {
      actions = document.createElement("div");
      actions.className = "chrome-actions chrome-bar-actions";
    }
    if (search && search.parentNode !== actions) actions.appendChild(search);

    titleRow.replaceChildren(brand, actions);
    titleRow.classList.add("chrome-row", "chrome-row-primary");
    titleRow.setAttribute("data-ias16-chrome", "ready");
  }

  function readView() {
    try {
      var stored = localStorage.getItem(KEY);
      if (stored === "mobile" || stored === "desktop") return stored;
    } catch (err) {}
    return "desktop";
  }

  function writeView(mode) {
    try { localStorage.setItem(KEY, mode); } catch (err) {}
  }

  function refit() {
    var api = window.cfIframeFit;
    if (!api || typeof api.fitAll !== "function") return;
    api.fitAll();
    requestAnimationFrame(function () {
      api.fitAll();
      setTimeout(api.fitAll, 50);
      setTimeout(api.fitAll, 250);
      setTimeout(api.fitAll, 600);
    });
  }

  function tuneScroll(bar) {
    var height = Math.ceil(bar.getBoundingClientRect().height);
    if (height < 1) return;
    document.documentElement.style.setProperty("--ias16-sticky-offset", (height + 16) + "px");
  }

  function markSearch() {
    var input = document.getElementById("chapterSearch");
    if (!input) return false;
    input.setAttribute("placeholder", "Find in IAS 16…");
    return true;
  }

  function mountMap(bar) {
    var iframe = document.querySelector(".visual-section iframe");
    var actions = bar.querySelector(".chrome-actions");
    if (!iframe || !actions) return;
    var fieldset = iframe.closest(".visual-fieldset") || iframe.parentNode;
    var viewport = iframe.closest(".map-viewport");
    if (!viewport) {
      viewport = document.createElement("div");
      viewport.className = "map-viewport";
      iframe.parentNode.insertBefore(viewport, iframe);
      viewport.appendChild(iframe);
    }
    var hint = fieldset.querySelector(".view-switch-hint");
    if (!hint) {
      hint = document.createElement("p");
      hint.className = "view-switch-hint";
      hint.textContent = HINT;
      fieldset.insertBefore(hint, viewport);
    }
    var group = actions.querySelector(".view-switch");
    if (!group) {
      group = document.createElement("div");
      group.className = "view-switch";
      group.setAttribute("role", "group");
      group.setAttribute("aria-label", "Concept Map view width");
      ["desktop", "mobile"].forEach(function (mode) {
        var btn = document.createElement("button");
        btn.type = "button";
        btn.className = "view-switch-btn";
        btn.setAttribute("data-view", mode);
        btn.textContent = mode === "desktop" ? "Desktop" : "Mobile";
        group.appendChild(btn);
      });
      var search = actions.querySelector(".chapter-search");
      if (search) actions.insertBefore(group, search);
      else actions.appendChild(group);
    }

    function apply(mode, persist) {
      var mobile = mode === "mobile";
      var name = mobile ? "mobile" : "desktop";
      viewport.setAttribute("data-view", name);
      hint.classList.toggle("is-on", mobile);
      var buttons = group.querySelectorAll(".view-switch-btn");
      for (var i = 0; i < buttons.length; i++) {
        var on = buttons[i].getAttribute("data-view") === name;
        buttons[i].setAttribute("aria-pressed", on ? "true" : "false");
      }
      if (persist) writeView(name);
      refit();
    }

    if (!group.getAttribute("data-wired")) {
      group.addEventListener("click", function (event) {
        var btn = event.target.closest(".view-switch-btn");
        if (!btn || !group.contains(btn)) return;
        apply(btn.getAttribute("data-view"), true);
      });
      group.setAttribute("data-wired", "1");
    }
    apply(readView(), false);
  }

  function boot() {
    if (!document.body || document.body.getAttribute("data-pack") !== "ias16") return;
    var bar = document.querySelector("header.chrome-bar");
    if (!bar) return;
    reshape(bar);
    mountMap(bar);
    tuneScroll(bar);
    markSearch();
    if (!markSearch()) requestAnimationFrame(markSearch);
    if (typeof ResizeObserver !== "undefined") {
      var observer = new ResizeObserver(function () { tuneScroll(bar); });
      observer.observe(bar);
    }
    window.addEventListener("resize", function () { tuneScroll(bar); });
  }

  if (document.body && document.body.getAttribute("data-pack") === "ias16") {
    var early = document.querySelector("header.chrome-bar");
    if (early) reshape(early);
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", boot);
  else boot();
})();
