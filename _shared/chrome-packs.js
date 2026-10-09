/* Pack titles and chapter pills for the shared top bar.
   Chapter pages do not copy this markup. chrome-bar.js reads it.
   chapters = row 2 pills. meta = links under the page H1. */
window.CHROME_PACKS = {
  ias16: {
    title: "IAS 16 Property, Plant and Equipment",
    search: "Find in IAS 16…",
    map: "index.html",
    chapters: [
      { href: "ch01.html", label: "1 Scope" },
      { href: "ch02.html", label: "2 Recognition" },
      { href: "ch03.html", label: "3 Initial measurement" },
      { href: "ch04.html", label: "4 Subsequent — models" },
      { href: "ch05.html", label: "5 Depreciation" },
      { href: "ch06.html", label: "6 Derecognition" },
      { href: "ch07.html", label: "7 Disclosure" }
    ],
    meta: [
      { href: "abbreviations.html", label: "Abbreviations" },
      { href: "references.html", label: "References" }
    ]
  },
  ias2: {
    title: "IAS 2 Inventories",
    search: "Find in IAS 2…",
    map: "index.html",
    chapters: [
      { href: "ch01.html", label: "1 Scope" },
      { href: "ch02.html", label: "2 Recognition" },
      { href: "ch03.html", label: "3 Initial measurement" },
      { href: "ch04.html", label: "4 Subsequent" },
      { href: "ch05.html", label: "5 Derecognition" },
      { href: "ch06.html", label: "6 Disclosure" }
    ],
    meta: [
      { href: "abbreviations.html", label: "Abbreviations" },
      { href: "references.html", label: "References" }
    ]
  },
  ifrs18: {
    title: "IFRS 18 Presentation and Disclosure",
    search: "Find in IFRS 18…",
    map: "index.html",
    chapters: [
      { href: "ch01.html", label: "1 What’s new" },
      { href: "ch02.html", label: "2 Aggregation" },
      { href: "ch03.html", label: "3 Categories" },
      { href: "ch04.html", label: "4 Subtotals" },
      { href: "ch05.html", label: "5 Expenses" },
      { href: "ch06.html", label: "6 MPMs" },
      { href: "ch07.html", label: "7 Other FS" },
      { href: "ch08.html", label: "8 Transition" }
    ],
    meta: [
      { href: "abbreviations.html", label: "Abbreviations" },
      { href: "references.html", label: "References" }
    ]
  },
  cf2018: {
    title: "Conceptual Framework 2018",
    search: "Find in the Framework…",
    map: "index.html",
    chapters: [
      { href: "ch01.html", label: "1 Objective" },
      { href: "ch02.html", label: "2 Qualitative" },
      { href: "ch03.html", label: "3 Entity" },
      { href: "ch04.html", label: "4 Elements" },
      { href: "ch05.html", label: "5 Recognition" },
      { href: "ch06.html", label: "6 Measurement" },
      { href: "ch07.html", label: "7 Presentation" },
      { href: "ch08.html", label: "8 Capital" },
      { href: "ch09.html", label: "9 Combined" },
      { href: "ch10.html", label: "10 Carve-out" },
      { href: "ch11.html", label: "11 Status" }
    ],
    meta: [
      { href: "references.html", label: "References" }
    ]
  }
};

window.CHROME_PACK_PATHS = [
  ["/ias-16/", "ias16"],
  ["/ias-2/", "ias2"],
  ["/ifrs-18/", "ifrs18"],
  ["/cf-2018/", "cf2018"]
];
