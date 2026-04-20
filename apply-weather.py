#!/usr/bin/env python3
"""Apply Weather System feature to Train Tracks index.html"""

import re

with open('index.html', 'r') as f:
    html = f.read()

# ============================================================
# 1. CSS: Weather particle animations + overlay tinting
# ============================================================

weather_css = """/* WEATHER PARTICLES */
@keyframes rain-fall {
  0% { opacity: 0.7; transform: translateY(0) translateX(var(--rain-dx, 0px)); }
  100% { opacity: 0; transform: translateY(var(--rain-dist, 120px)) translateX(var(--rain-dx, -3px)); }
}
@keyframes snow-fall {
  0% { opacity: 0.8; transform: translateY(0) translateX(0) rotate(0deg); }
  50% { opacity: 0.9; transform: translateY(var(--snow-half, 60px)) translateX(var(--snow-drift, 15px)) rotate(180deg); }
  100% { opacity: 0; transform: translateY(var(--snow-dist, 120px)) translateX(var(--snow-drift-end, -5px)) rotate(360deg); }
}
.rain-particle {
  position: absolute;
  width: 2px;
  border-radius: 0 0 2px 2px;
  background: linear-gradient(to bottom, rgba(120,180,255,0), rgba(120,180,255,0.7));
  pointer-events: none;
  z-index: 75;
  animation: rain-fall var(--rain-speed, 0.6s) linear forwards;
}
.snow-particle {
  position: absolute;
  border-radius: 50%;
  background: rgba(255,255,255,0.85);
  pointer-events: none;
  z-index: 75;
  box-shadow: 0 0 3px rgba(255,255,255,0.5);
  animation: snow-fall var(--snow-speed, 3s) ease-in forwards;
}

/* Weather overlay tinting */
#weather-overlay {
  position: absolute;
  top: 0; left: 0;
  width: 100%; height: 100%;
  pointer-events: none;
  z-index: 70;
  border-radius: 12px;
  transition: background 0.8s ease;
}
.weather-rain #weather-overlay {
  background: rgba(60,80,120,0.12);
}
.weather-snow #weather-overlay {
  background: rgba(200,220,240,0.1);
}
body.night-mode .weather-rain #weather-overlay {
  background: rgba(20,30,50,0.15);
}
body.night-mode .weather-snow #weather-overlay {
  background: rgba(100,120,150,0.1);
}

"""

html = html.replace('/* Reduced Motion Preference */', weather_css + '/* Reduced Motion Preference */')

# Add weather particles to reduced motion block
html = html.replace(
    '  .water-cell::before, .water-cell::after {\n    animation: none !important;\n  }',
    '  .water-cell::before, .water-cell::after {\n    animation: none !important;\n  }\n  .rain-particle, .snow-particle {\n    animation: none !important;\n    display: none !important;\n  }'
)

# ============================================================
# 2. HTML: Weather overlay div inside grid-viewport
# ============================================================

html = html.replace(
    '      <div id="zoom-indicator">1.0\u00d7</div>\n    </div>',
    '      <div id="weather-overlay"></div>\n      <div id="zoom-indicator">1.0\u00d7</div>\n    </div>'
)

# ============================================================
# 3. HTML: Weather toggle button in controls (after biome button)
# ============================================================

html = html.replace(
    '      <button class="btn" id="btn-biome" onclick="cycleBiome()"',
    '      <button class="btn" id="btn-weather" onclick="cycleWeather()" style="background:#5C9DC5;color:white;box-shadow:0 3px 10px rgba(92,157,197,0.3);padding:8px 12px;" title="Change weather (W)">☀️</button>\n      <button class="btn" id="btn-biome" onclick="cycleBiome()"'
)

# ============================================================
# 4. HTML: Weather keyboard shortcut in shortcuts modal
# ============================================================

html = html.replace(
    '    <div class="shortcut-row"><span class="shortcut-desc">Cycle biome</span><span class="shortcut-key">B</span></div>',
    '    <div class="shortcut-row"><span class="shortcut-desc">Cycle biome</span><span class="shortcut-key">B</span></div>\n    <div class="shortcut-row"><span class="shortcut-desc">Cycle weather</span><span class="shortcut-key">W</span></div>'
)

# ============================================================
# 5. JS: Weather state constants and variables (after BIOME system)
# ============================================================

weather_js = """
// WEATHER SYSTEM
const WEATHER_MODES = ['sunny', 'rain', 'snow'];
const WEATHER_KEY = 'trainTracks_weather';
const WEATHER_ICONS = { sunny: '☀️', rain: '🌧️', snow: '❄️' };
const WEATHER_NAMES = { sunny: 'Sunny', rain: 'Rainy', snow: 'Snowy' };
let currentWeather = 'sunny';
let weatherInterval = null;
let weatherParticles = [];
const MAX_WEATHER_PARTICLES = 60;
let weatherAmbientNodes = []; // active ambient sound oscillators/nodes
let weatherAmbientGain = null;

"""

html = html.replace(
    "let currentBiome = 'spring';",
    "let currentBiome = 'spring';" + weather_js
)

# ============================================================
# 6. JS: Weather functions (after restoreBiome function block)
# ============================================================

# Find the end of restoreBiome function
weather_functions = """
// ============================================================
// WEATHER SYSTEM — Rain, Snow, Sunny
// ============================================================
function cycleWeather() {
  const idx = WEATHER_MODES.indexOf(currentWeather);
  const newWeather = WEATHER_MODES[(idx + 1) % WEATHER_MODES.length];
  applyWeather(newWeather);
  try { localStorage.setItem(WEATHER_KEY, newWeather); } catch (e) {}
  showToast(WEATHER_ICONS[newWeather] + ' ' + WEATHER_NAMES[newWeather] + ' weather!');
}

function applyWeather(weather) {
  // Remove old weather classes from viewport
  const vp = document.getElementById('grid-viewport');
  if (vp) {
    vp.classList.remove('weather-rain', 'weather-snow');
    if (weather !== 'sunny') {
      vp.classList.add('weather-' + weather);
    }
  }
  // Stop old weather systems
  stopWeatherParticles();
  stopWeatherAmbient();
  currentWeather = weather;
  // Update button
  const btn = document.getElementById('btn-weather');
  if (btn) btn.textContent = WEATHER_ICONS[weather];
  // Start new weather
  if (weather !== 'sunny') {
    startWeatherParticles();
    startWeatherAmbient();
  }
}

function restoreWeather() {
  try {
    const saved = localStorage.getItem(WEATHER_KEY);
    if (saved && WEATHER_MODES.includes(saved)) {
      applyWeather(saved);
    }
  } catch (e) {}
}

// --- Weather Particles ---
function startWeatherParticles() {
  stopWeatherParticles();
  if (prefersReducedMotion()) return;
  const rate = currentWeather === 'rain' ? 40 : 200; // ms between spawns
  weatherInterval = setInterval(spawnWeatherParticle, rate);
}

function stopWeatherParticles() {
  if (weatherInterval) { clearInterval(weatherInterval); weatherInterval = null; }
  // Clean up existing particles
  weatherParticles.forEach(p => { if (p.parentNode) p.remove(); });
  weatherParticles = [];
  // Also remove any orphaned weather particles from DOM
  document.querySelectorAll('.rain-particle, .snow-particle').forEach(el => el.remove());
}

function spawnWeatherParticle() {
  if (prefersReducedMotion()) return;
  const vp = document.getElementById('grid-viewport');
  if (!vp) return;

  // Recycle old particles
  if (weatherParticles.length >= MAX_WEATHER_PARTICLES) {
    const old = weatherParticles.shift();
    if (old.parentNode) old.remove();
  }

  const vpW = vp.clientWidth;
  const vpH = vp.clientHeight;

  const particle = document.createElement('div');

  if (currentWeather === 'rain') {
    particle.className = 'rain-particle';
    const height = 8 + Math.random() * 12;
    const speed = 0.4 + Math.random() * 0.3;
    const dx = -2 + Math.random() * -3;
    particle.style.height = height + 'px';
    particle.style.left = (Math.random() * vpW) + 'px';
    particle.style.top = (-height) + 'px';
    particle.style.setProperty('--rain-speed', speed + 's');
    particle.style.setProperty('--rain-dist', vpH + 'px');
    particle.style.setProperty('--rain-dx', dx + 'px');
  } else if (currentWeather === 'snow') {
    particle.className = 'snow-particle';
    const size = 3 + Math.random() * 5;
    const speed = 2.5 + Math.random() * 2.5;
    const drift = -20 + Math.random() * 40;
    const driftEnd = -15 + Math.random() * 30;
    particle.style.width = size + 'px';
    particle.style.height = size + 'px';
    particle.style.left = (Math.random() * vpW) + 'px';
    particle.style.top = (-size) + 'px';
    particle.style.setProperty('--snow-speed', speed + 's');
    particle.style.setProperty('--snow-dist', vpH + 'px');
    particle.style.setProperty('--snow-half', (vpH / 2) + 'px');
    particle.style.setProperty('--snow-drift', drift + 'px');
    particle.style.setProperty('--snow-drift-end', driftEnd + 'px');
  }

  vp.appendChild(particle);
  weatherParticles.push(particle);

  // Auto-remove after animation
  const dur = parseFloat(particle.style.getPropertyValue(
    currentWeather === 'rain' ? '--rain-speed' : '--snow-speed'
  )) * 1000 + 100;
  setTimeout(() => {
    const idx = weatherParticles.indexOf(particle);
    if (idx >= 0) weatherParticles.splice(idx, 1);
    if (particle.parentNode) particle.remove();
  }, dur);
}

// --- Weather Ambient Sound ---
function startWeatherAmbient() {
  if (!soundEnabled) return;
  const ctx = getAudioCtx();
  if (!ctx) return;
  stopWeatherAmbient();

  weatherAmbientGain = ctx.createGain();
  weatherAmbientGain.gain.value = 0;
  weatherAmbientGain.connect(getMasterGain());

  if (currentWeather === 'rain') {
    // Rain: filtered brown noise
    const bufSize = ctx.sampleRate * 2;
    const buf = ctx.createBuffer(1, bufSize, ctx.sampleRate);
    const data = buf.getChannelData(0);
    let lastOut = 0;
    for (let i = 0; i < bufSize; i++) {
      const white = Math.random() * 2 - 1;
      lastOut = (lastOut + (0.02 * white)) / 1.02;
      data[i] = lastOut * 3.5;
    }
    const src = ctx.createBufferSource();
    src.buffer = buf;
    src.loop = true;
    const hpf = ctx.createBiquadFilter();
    hpf.type = 'highpass';
    hpf.frequency.value = 400;
    const lpf = ctx.createBiquadFilter();
    lpf.type = 'lowpass';
    lpf.frequency.value = 3000;
    src.connect(hpf);
    hpf.connect(lpf);
    lpf.connect(weatherAmbientGain);
    src.start();
    weatherAmbientNodes.push(src);
    // Fade in
    weatherAmbientGain.gain.linearRampToValueAtTime(0.08, ctx.currentTime + 1.5);

  } else if (currentWeather === 'snow') {
    // Snow: gentle wind — very soft filtered noise
    const bufSize = ctx.sampleRate * 2;
    const buf = ctx.createBuffer(1, bufSize, ctx.sampleRate);
    const data = buf.getChannelData(0);
    let lastOut = 0;
    for (let i = 0; i < bufSize; i++) {
      const white = Math.random() * 2 - 1;
      lastOut = (lastOut + (0.01 * white)) / 1.01;
      data[i] = lastOut * 2;
    }
    const src = ctx.createBufferSource();
    src.buffer = buf;
    src.loop = true;
    const lpf = ctx.createBiquadFilter();
    lpf.type = 'lowpass';
    lpf.frequency.value = 800;
    src.connect(lpf);
    lpf.connect(weatherAmbientGain);
    src.start();
    weatherAmbientNodes.push(src);
    // Fade in softly
    weatherAmbientGain.gain.linearRampToValueAtTime(0.04, ctx.currentTime + 2);
  }
}

function stopWeatherAmbient() {
  weatherAmbientNodes.forEach(node => {
    try { node.stop(); } catch (e) {}
    try { node.disconnect(); } catch (e) {}
  });
  weatherAmbientNodes = [];
  if (weatherAmbientGain) {
    try { weatherAmbientGain.disconnect(); } catch (e) {}
    weatherAmbientGain = null;
  }
}

"""

html = html.replace(
    "function restoreBiome() {\n  try {\n    const saved = localStorage.getItem(BIOME_KEY);",
    weather_functions + "function restoreBiome() {\n  try {\n    const saved = localStorage.getItem(BIOME_KEY);"
)

# ============================================================
# 7. JS: 'W' keyboard shortcut (after B for biome)
# ============================================================

html = html.replace(
    "  // B: cycle biome\n  if ((key === 'b' || key === 'B') && !e.ctrlKey && !e.metaKey) {\n    cycleBiome();\n    return;\n  }",
    "  // B: cycle biome\n  if ((key === 'b' || key === 'B') && !e.ctrlKey && !e.metaKey) {\n    cycleBiome();\n    return;\n  }\n\n  // W: cycle weather\n  if ((key === 'w' || key === 'W') && !e.ctrlKey && !e.metaKey) {\n    cycleWeather();\n    return;\n  }"
)

# ============================================================
# 8. JS: Restore weather in init() (after restoreBiome)
# ============================================================

html = html.replace(
    "  // Restore biome preference\n  restoreBiome();",
    "  // Restore biome preference\n  restoreBiome();\n\n  // Restore weather preference\n  restoreWeather();"
)

# ============================================================
# 9. JS: Pause/resume weather on visibility change
# ============================================================

html = html.replace(
    "      stopChimneyLoop();\n      stopMusicLoop();",
    "      stopChimneyLoop();\n      stopMusicLoop();\n      stopWeatherParticles();\n      stopWeatherAmbient();"
)

html = html.replace(
    "      startChimneyLoop();\n      if (musicEnabled) startMusicLoop();",
    "      startChimneyLoop();\n      if (musicEnabled) startMusicLoop();\n      if (currentWeather !== 'sunny') { startWeatherParticles(); startWeatherAmbient(); }"
)

# ============================================================
# 10. JS: Clean up weather particles in clearAll (before renderAllCells)
# ============================================================
# Not strictly needed since weather is independent of board state, but good hygiene

# ============================================================
# 11. JS: Stop weather ambient in stopPlay audio cleanup? No - weather is ambient, not play-dependent
# ============================================================

# ============================================================
# Verify no duplicate insertions
# ============================================================
count_weather_key = html.count("const WEATHER_KEY")
count_cycle_weather = html.count("function cycleWeather()")
count_apply_weather = html.count("function applyWeather(weather)")
count_btn_weather = html.count("id=\"btn-weather\"")

assert count_weather_key == 1, f"WEATHER_KEY appears {count_weather_key} times"
assert count_cycle_weather == 1, f"cycleWeather appears {count_cycle_weather} times"
assert count_apply_weather == 1, f"applyWeather appears {count_apply_weather} times"
assert count_btn_weather == 1, f"btn-weather appears {count_btn_weather} times"

with open('index.html', 'w') as f:
    f.write(html)

print("✅ Weather system applied successfully!")
print(f"  - WEATHER_KEY: {count_weather_key}")
print(f"  - cycleWeather: {count_cycle_weather}")
print(f"  - applyWeather: {count_apply_weather}")
print(f"  - btn-weather: {count_btn_weather}")
