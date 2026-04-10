# Day 22 Build Report — Screenshot & Download

## Changes Made

### CSS (added ~70 lines)
- `#screenshot-overlay` — fullscreen modal backdrop with blur
- `#screenshot-modal` — centered modal card (520px max, responsive)
- `#screenshot-preview` — canvas preview with rounded border
- `.screenshot-actions` — flex row for download/copy buttons
- `.btn-download-screenshot` — green download button
- `.btn-copy-screenshot` — blue copy button

### HTML
1. **Controls bar**: Added 📸 screenshot button (indigo `#5C6BC0`) before the ❓ help button
2. **Screenshot modal**: Full modal with `<canvas id="screenshot-preview">`, download and copy buttons, close button. Positioned after puzzle overlay.
3. **Shortcuts modal**: Added "Screenshot — P" row under Display section

### JavaScript (added ~280 lines)
1. **`renderScreenshotCanvas()`** — Core rendering function that creates a high-res canvas (4x scale = 2880×1924px):
   - Reads CSS custom properties for current theme (biome + night mode aware)
   - Renders grass background, water cells with wave lines
   - Renders all track types (straight, curve, T-junction, crossover, bridge, tunnel, station) with bed/track/ties
   - Renders scenery as emoji text via `getSceneryEmoji()` (biome-aware)
   - Renders trains as colored circles with emoji overlay
   - Renders connection dots (green/red) with glow effects
   - Uses canvas transform (translate+rotate) for rotated pieces

2. **`openScreenshotModal()`** — Renders screenshot, displays in preview canvas, opens modal
3. **`closeScreenshotModal()`** — Closes modal, clears canvas reference
4. **`closeScreenshotModalOutside(e)`** — Click-outside-to-close handler
5. **`downloadScreenshot()`** — Uses `canvas.toBlob()` → `URL.createObjectURL()` → anchor click download. File named `train-tracks-YYYY-MM-DD.png`
6. **`copyScreenshot()`** — Uses `canvas.toBlob()` → `ClipboardItem` → `navigator.clipboard.write()`. Falls back gracefully.

### Keyboard Shortcut
- `P` key opens screenshot modal (only when not in modal, not playing, not typing in input)
- `Escape` closes screenshot modal (added to escape handler chain)
- Screenshot modal blocks other shortcuts when open

## Implementation Notes
- Used canvas-based rendering rather than DOM capture for clean, chrome-free output
- 4x scale provides crisp output even on retina displays
- Track rendering uses simplified but recognizable versions of the SVG track pieces
- Tunnel rendering includes mountain shape with dark oval opening
- All rendering is synchronous — no async image loading needed
