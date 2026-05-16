# Social preview (OG image) spec

GitHub recommends **1280 × 640 px** for repo social previews. Twitter/X uses
the same aspect for `summary_large_image`.

## Design suggestion

Layout (left-to-right):

```
┌──────────────────────────────────────────────────────────┐
│                                                          │
│  octalum-bdtb                          [logo]     │
│  ───────────────────                                     │
│                                                          │
│  From brain to build in 60 seconds.                      │
│                                                          │
│  raw text  ──►  STRUCTURE · STACK · PHASES · RISKS       │
│                                                          │
│                                            harery.com    │
└──────────────────────────────────────────────────────────┘
```

## Typography

- **Headline:** Inter Bold, 96px, near-black (`#0F172A`)
- **Tagline:** Inter Medium, 48px, slate (`#475569`)
- **Workflow row:** JetBrains Mono, 32px, amber (`#D97706`) for the arrow,
  slate for the file names

## Colour palette

| Use         | Hex      | Notes                            |
|-------------|----------|----------------------------------|
| Background  | `#F8FAFC` | Off-white, easy on eyes         |
| Primary     | `#0F172A` | Near-black for headline         |
| Secondary   | `#475569` | Slate for body text             |
| Accent      | `#D97706` | Amber — matches "brain" warmth  |
| Border      | `#E2E8F0` | Subtle frame                     |

## Production options

1. **Figma** — create a 1280×640 frame, export as PNG. Save to `docs/og-image.png`.
2. **Carbon/Excalidraw** quick-and-dirty — fine for v0.1, replace before v1.0.
3. **Programmatic** — `Pillow` script (would add a dev-only dep; skipping for v0.1).

## Where to place it

1. Commit to `docs/og-image.png`.
2. In repo Settings → General → "Social preview", upload the PNG.
3. Add `<meta property="og:image" content="…/docs/og-image.png">` if you mirror the README to a site.

## Checklist before publishing

- [ ] Headline visible at 320×160 thumbnail size
- [ ] No PII / personal email in the image
- [ ] Contrast passes WCAG AA (use https://webaim.org/resources/contrastchecker)
- [ ] File ≤ 1 MB (GitHub limit)
