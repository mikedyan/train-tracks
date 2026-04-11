# Day 23 Build Report — Share Link

**Date:** 2026-04-11
**Feature:** Share Link (Compact URL encoding of grid state)

## What Was Built

### 1. Grid State Encoding (`encodeGridState()`)
- Binary format: version byte + 1 byte per cell (5 bits type + 2 bits rotation) + trains + switches
- Type mapping: 0=empty, 1-7=track types, 8-16=scenery types (all 16 types covered)
- Base64url encoding for URL-safe hash (no padding, `-` and `_` instead of `+` and `/`)
- Train encoding: count + [row, col, colorIdx, carCount, ...carTypes] per train
- Switch state encoding: count + [row, col, value] per switch

### 2. Grid State Decoding (`decodeGridState()`)
- Reverse of encoding with full validation
- Version check (currently v1)
- Bounds checking on all values
- Graceful failure (returns false on any error, no crash)

### 3. Share Link Button
- 🔗 button added in controls bar between biome and screenshot buttons
- Teal color (#26A69A) for visual distinction
- On click: encodes state → builds URL with `#s=` prefix → copies to clipboard
- Fallback clipboard method for older browsers (document.execCommand)
- Toast: "🔗 Link copied!"
- Blocked during puzzle mode with toast

### 4. Hash Detection on Page Load
- `loadFromShareHash()` called in `init()` BEFORE autoLoad
- Detects `#s=` prefix in URL hash
- Decodes and loads layout, then clears hash from URL (history.replaceState)
- Shows toast: "📂 Loaded shared layout!"
- If no hash or invalid hash, falls through to normal autoLoad

### 5. Keyboard Shortcut
- `L` key copies share link (same as clicking button)
- Blocked during play, in modals, in text inputs
- Added to shortcuts modal

## URL Size Analysis
- Empty grid: ~132 chars hash
- Typical layout: ~140-170 chars hash  
- Worst case (all cells filled, 3 trains with 5 cars each, 10 switches): ~208 chars hash
- Full URL with domain: < 260 chars worst case
- Well within the < 500 char spec requirement

## Technical Details
- Uses 1 byte per cell (not bit-packed) for simplicity and decode speed
- Base64url encoding adds ~33% overhead but avoids URL encoding issues
- Version byte allows future format changes
- No compression needed — raw format is compact enough

## Files Modified
- `index.html`: +223 lines (HTML button, JS functions, shortcut modal entry, keyboard shortcut)
