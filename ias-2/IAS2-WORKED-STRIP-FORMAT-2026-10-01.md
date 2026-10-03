# IAS 2 worked-strip format fix — 2026-10-01

- Standardised worked-strip peer body typography in `draft-v1-linked/assets/shared.css` at 13px ink, 1.45 line-height; list spacing is reset consistently.
- Made worked-strip titles flex column rows and wrapped citation chips in `.cite-row`.
- HTML-fixed all 38 worked-strip titles across ch01–ch05; ch06 has no worked-strips. No invalid `<p class="box-body"><ul>` wrappers were present.
- `/refs/ias-2/preview/` is a symlink to `draft-v1-linked`, so it is synced automatically. The requested Documents twin path was not present on the box.
