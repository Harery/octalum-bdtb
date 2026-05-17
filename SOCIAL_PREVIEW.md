# Social preview (OG image) spec

GitHub recommends **1280 × 640 px** for repo social previews. Twitter/X uses
the same aspect for `summary_large_image`.

## Design suggestion

Layout (left-to-right):

```
┌──────────────────────────────────────────────────────────┐
│  DWG. octalum-bdtb.04           PHASE-0 · OCTALUM FAMILY │
│ ─────────────────────────────────────────────────────────│
│                                                          │
│            octalum-bdtb.                                 │
│                                                          │
│  A 12-stage Claude Code Skill — customer brain-dump →    │
│  delivered product, with AI doing 90-95% of the work.    │
│                                                          │
│ ─────────────────────────────────────────────────────────│
│  HARERY.COM  ·  ARCHITECT       GITHUB.COM/HARERY/...    │
└──────────────────────────────────────────────────────────┘
```

A pre-rendered PNG matching the OCTALUM family BLUEPRINT aesthetic
(paper `#EFEBE0` / ink `#1A2330` / accent `#B23A48`) lives at
[`.github/assets/social-preview.png`](.github/assets/social-preview.png)
and [`docs/assets/social-preview.png`](docs/assets/social-preview.png).
Upload either via repo Settings → Social preview.

## Typography (OCTALUM family BLUEPRINT theme)

- **Headline:** Georgia Bold (Fraunces in print), 120px, ink `#1A2330`
- **Italic suffix + red accent period:** Georgia Italic, 120px, accent `#B23A48`
- **Tagline:** Georgia Italic, auto-fit 22-34px, ink at 200/255 opacity
- **DWG / family label:** Courier New, 18px, ink + accent

## Colour palette (BLUEPRINT family — same across all 5 repos)

| Use         | Hex       | Notes                                |
|-------------|-----------|--------------------------------------|
| Background  | `#EFEBE0` | Warm paper cream                     |
| Primary     | `#1A2330` | Deep navy ink                        |
| Secondary   | `#1A2330` @ 60% | Ink muted for taglines         |
| Accent      | `#B23A48` | Paper-architectural red              |
| Grid lines  | `#1A2330` @ 2% | Subtle 32px grid background     |

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
