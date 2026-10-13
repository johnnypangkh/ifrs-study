/* SOURCE ias-16/draft-v1-linked/visuals/master-concept-map.html @ cfc59d2b
   Five matchMedia("(max-width: 800px)") branches. Live file keeps the not-narrow path only.
   Line numbers are the base file. */

/* dockImpair L1353-L1356 */
    if (window.matchMedia("(max-width: 800px)").matches) {
      flow.style.removeProperty("--shaft-x");
      return;
    }

/* sizeAxisName L1370-L1374 */
    if (window.matchMedia("(max-width: 800px)").matches) {
      if (name.style.minHeight) name.style.minHeight = "";
      if (rule && rule.style.marginTop) rule.style.marginTop = "";
      return;
    }

/* alignLedgers L1416-L1420 */
    var narrow = window.matchMedia("(max-width: 800px)").matches;
    for (var g = 0; g < terms.length; g++) {
      for (var j = 0; j < terms[g].length; j++) terms[g][j].style.minHeight = "0px";
    }
    if (narrow || terms.length < 2) return;

/* drawConnectors narrow flag L1446-L1446 */
    var narrow = window.matchMedia("(max-width: 800px)").matches;

/* vFlow narrow label L1460-L1461 */
      if (narrow) placeLabel(lab, x - em(0.55), (y1 + y2) / 2, "left");
      else placeLabel(lab, x + em(0.55), (y1 + y2) / 2, "right");

/* fork-ppe narrow connector L1479-L1480 */
      if (narrow) hFlow(leaf1.cy, q1.cx, leaf1.l, noLab, "mute");
      else hFlow(q1.cy, q1.r, leaf1.l, noLab, "mute");

/* fork-excl narrow connector L1491-L1492 */
      if (narrow) hFlow(leaf3.cy, q3.cx, leaf3.l, yesLab, "stop");
      else hFlow(q3.cy, q3.r, leaf3.l, yesLab, "stop");

/* recog rail narrow connector L1501-L1505 */
    if (narrow && shown(recogRail) && shown(capQ)) {
      var railB = boxOf(recogRail);
      var q2 = boxOf(capQ);
      vFlow(railB.cx, railB.b, q2.t, null);
    }

/* fork-cap narrow connector L1511-L1512 */
      if (narrow) hFlow(leafY.cy, qY.cx, leafY.l, capNo, "mute");
      else hFlow(qY.cy, qY.r, leafY.l, capNo, "mute");

/* cap yes narrow condition L1518-L1518 */
      if (narrow || Math.abs(qYes.cx - plate.cx) <= 3) {

/* linkStem narrow guard L1529-L1532 */
    if (!narrow) {
      linkStem(root.querySelector(".cost-result"), root.querySelector(".nature-nest > .port-tab"));
      linkStem(root.querySelector(".da-col"), root.querySelector(".ready-axis > .axis-port"));
    }

/* pack-flow narrow connector L1573-L1579 */
      if (narrow && shown(rail) && rail.classList.contains("rail-link")) {
        var R = boxOf(rail);
        vFlow(S.cx, S.b, R.t, flowLab);
        vFlow(R.cx, R.b, T.t, null);
      } else {
        vFlow(S.cx, S.b, T.t, flowLab);
      }

/* policy parent narrow guard L1584-L1584 */
    if (!narrow && shown(parent) && heads.length >= 2 && shown(heads[0]) && shown(heads[1])) {

/* fit narrow rail clear L1625-L1635 */
    var narrow = window.matchMedia("(max-width: 800px)").matches;
    var rails = root.querySelectorAll(".rail-link[data-phase]");
    for (var i = 0; i < rails.length; i++) {
      var rail = rails[i];
      if (narrow) {
        if (rail.style.marginTop || rail.style.height) {
          rail.style.marginTop = "";
          rail.style.height = "";
        }
        continue;
      }
