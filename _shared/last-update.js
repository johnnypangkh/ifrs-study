/* One Last update stamp for a pack.
   The time already on that pack is the only time. Pages mount an empty
   span.chrome-last-update; this file fills it. */
(function () {
  var STAMPS = {
    ias2: {
      text: "Last update · 2 Oct 2026, 16:03 HKT",
      iso: "2026-10-02T16:03:00+08:00"
    },
    ifrs18: {
      text: "Last update · 2026-10-02 20:16 HKT",
      iso: "2026-10-02T20:16:00+08:00"
    },
    cf2018: {
      text: "Last update · 2026-10-03 00:20 HKT",
      iso: "2026-10-03T00:20:00+08:00"
    }
  };

  function packId() {
    var body = document.body;
    var fromBody = body && body.getAttribute("data-pack");
    if (fromBody && STAMPS[fromBody]) return fromBody;
    var path = location.pathname || "";
    if (path.indexOf("/ias-2/") !== -1) return "ias2";
    if (path.indexOf("/ifrs-18/") !== -1) return "ifrs18";
    if (path.indexOf("/cf-2018/") !== -1) return "cf2018";
    return "";
  }

  function mount() {
    var stamp = STAMPS[packId()];
    if (!stamp) return false;
    var el = document.querySelector("span.chrome-last-update");
    if (!el) {
      var host = document.querySelector(".chrome-title-cluster") || document.querySelector(".chrome-bar-title");
      if (!host) return false;
      el = document.createElement("span");
      el.className = "chrome-last-update";
      host.appendChild(el);
    }
    if (el.getAttribute("data-last-update-ready") === "true") return true;
    el.textContent = stamp.text;
    el.setAttribute("data-last-update", stamp.iso);
    el.removeAttribute("title");
    el.setAttribute("data-last-update-ready", "true");
    return true;
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", mount);
  } else {
    mount();
  }
})();
