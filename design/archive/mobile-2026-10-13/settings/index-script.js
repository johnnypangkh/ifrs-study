/* SOURCE site/settings/index.html script @ cfc59d2b */
(function () {
  var scope = document.querySelector(".settings-preview");
  function apply() {
    var parts = location.hash.replace(/^#/, "").split(",").filter(Boolean);
    var mobile = parts.indexOf("m") >= 0;
    var day = parts.indexOf("light") >= 0;
    document.body.classList.toggle("mode-m", mobile);
    document.body.classList.toggle("mode-d", !mobile);
    document.body.classList.toggle("theme-light", day);
    scope.setAttribute("data-theme", day ? "light" : "dark");
    var cells = scope.querySelectorAll(".pv");
    for (var i = 0; i < cells.length; i++) cells[i].classList.toggle("is-mobile", mobile);
    var buttons = document.querySelectorAll(".seg button");
    for (var j = 0; j < buttons.length; j++) {
      var key = buttons[j].getAttribute("data-set");
      var on = (key === "m" && mobile) || (key === "d" && !mobile) || (key === "light" && day) || (key === "dark" && !day);
      buttons[j].classList.toggle("on", on);
    }
  }
  var controls = document.querySelectorAll(".seg button");
  for (var n = 0; n < controls.length; n++) {
    controls[n].addEventListener("click", function (event) {
      var button = event.currentTarget;
      var parts = location.hash.replace(/^#/, "").split(",").filter(Boolean);
      var key = button.getAttribute("data-set");
      parts = parts.filter(function (token) {
        return (key === "m" || key === "d") ? token !== "m" : token !== "light";
      });
      if (key === "m" || key === "light") parts.push(key);
      location.hash = parts.join(",");
    });
  }
  window.addEventListener("hashchange", apply);
  apply();
})();
