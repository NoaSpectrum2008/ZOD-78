# Streamlit en utilities van utils.py importeren
import streamlit as s
from utils import fake_delay, glitch_text

# AI GEBRUIKT VOOR DE CSS SUPERCOMPUTER!!!
def inject_theme_css():
    s.markdown(
        """
<style>
/* ------- SUPERCOMPUTER / YEAR 3060 LOOK ------- */
:root{
  --bg0:#05060a;
  --bg1:#070b16;
  --neon:#65ffb5;
  --neon2:#7ae7ff;
  --warn:#ff3b7a;
  --amber:#ffcc66;
  --panel:rgba(8, 14, 18, 0.72);
  --line:rgba(101,255,181,0.18);
}

/* achtergrond + neon gloed */
html, body, [data-testid="stAppViewContainer"]{
  background:
    radial-gradient(900px 400px at 15% 10%, rgba(122,231,255,0.16), transparent 60%),
    radial-gradient(800px 450px at 85% 20%, rgba(255,59,122,0.10), transparent 60%),
    radial-gradient(650px 380px at 45% 80%, rgba(101,255,181,0.10), transparent 55%),
    linear-gradient(135deg, var(--bg0), var(--bg1));
  color: rgba(220,255,240,0.95);
}

/* scanlines */
[data-testid="stAppViewContainer"]::before{
  content:"";
  position: fixed;
  inset:0;
  pointer-events:none;
  background: repeating-linear-gradient(
    to bottom,
    rgba(255,255,255,0.03),
    rgba(255,255,255,0.03) 1px,
    rgba(0,0,0,0) 3px,
    rgba(0,0,0,0) 7px
  );
  mix-blend-mode: overlay;
  opacity: 0.35;
  z-index: 9998;
}

/* flicker effect */
@keyframes flicker {
  0%{opacity:1}
  3%{opacity:.92}
  6%{opacity:1}
  8%{opacity:.88}
  10%{opacity:1}
  100%{opacity:1}
}
[data-testid="stAppViewContainer"]{ animation: flicker 6s infinite; }

/* “sparks / explosies” vibe (heel licht) */
@keyframes sparks {
  0%   { transform: translate(0,0) scale(1); opacity: 0; }
  10%  { opacity: .22; }
  40%  { opacity: .16; }
  100% { transform: translate(30px, 80px) scale(1.5); opacity: 0; }
}
[data-testid="stAppViewContainer"]::after{
  content:"";
  position: fixed;
  inset:-20%;
  pointer-events:none;
  z-index: 9997;
  background:
    radial-gradient(2px 2px at 20% 30%, rgba(255,59,122,0.9), transparent 60%),
    radial-gradient(2px 2px at 70% 22%, rgba(255,204,102,0.9), transparent 60%),
    radial-gradient(1px 1px at 60% 80%, rgba(122,231,255,0.9), transparent 60%),
    radial-gradient(2px 2px at 35% 65%, rgba(101,255,181,0.9), transparent 60%);
  opacity: 0;
  animation: sparks 7s infinite;
}

/* titels */
h1,h2,h3{
  color: var(--neon);
  letter-spacing: .08em;
  text-transform: uppercase;
}

/* sidebar */
[data-testid="stSidebar"]{
  background: linear-gradient(180deg, rgba(8,14,18,0.9), rgba(8,14,18,0.6));
  border-right: 1px solid var(--line);
}

/* HUD panel */
.hud-panel{
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: 16px;
  padding: 14px 14px;
  box-shadow: 0 0 0 1px rgba(122,231,255,0.08), 0 18px 55px rgba(0,0,0,0.35);
}
.hud-top{ display:flex; align-items:center; justify-content:space-between; gap: 12px; }
.hud-title{ font-weight: 800; color: var(--neon2); letter-spacing: .14em; }
.hud-sub{ font-size: 12px; color: rgba(210,255,235,0.70); }

/* status lights */
.lights{ display:flex; gap:8px; align-items:center; }
.light{
  width:10px; height:10px; border-radius:999px;
  border: 1px solid rgba(255,255,255,0.15);
}
@keyframes pulse { 0%{transform:scale(1);opacity:.65} 50%{transform:scale(1.2);opacity:1} 100%{transform:scale(1);opacity:.65} }
.green{ background: rgba(101,255,181,0.85); box-shadow: 0 0 14px rgba(101,255,181,0.35); animation:pulse 1.8s infinite; }
.blue { background: rgba(122,231,255,0.85); box-shadow: 0 0 14px rgba(122,231,255,0.30); animation:pulse 2.4s infinite; }
.red  { background: rgba(255,59,122,0.85);  box-shadow: 0 0 16px rgba(255,59,122,0.35);  animation:pulse 1.2s infinite; }

/* buttons -> voelen als machine knoppen */
.stButton>button{
  width:100%;
  background: linear-gradient(180deg, rgba(20,40,34,0.75), rgba(10,16,14,0.70));
  color: rgba(220,255,240,0.95);
  border: 1px solid rgba(101,255,181,0.35);
  border-radius: 14px;
  padding: 0.85rem 1rem;
  letter-spacing: .14em;
  text-transform: uppercase;
  box-shadow: 0 0 0 1px rgba(122,231,255,0.07), 0 14px 40px rgba(0,0,0,0.35);
  transition: transform .08s ease, border-color .12s ease, filter .12s ease;
}
.stButton>button:active{
  transform: translateY(2px);
  border-color: rgba(255,59,122,0.65);
  filter: brightness(1.15);
}

/* console paneel */
.console{
  background: rgba(0,0,0,0.48);
  border: 1px solid rgba(101,255,181,0.22);
  border-radius: 16px;
  padding: 12px 14px;
  font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono","Courier New", monospace;
  color: rgba(220,255,240,0.93);
  box-shadow: inset 0 0 0 1px rgba(122,231,255,0.06);
}
.console .err{ color: rgba(255,59,122,0.95); }
.console .ok{ color: rgba(101,255,181,0.95); }
.console .inf{ color: rgba(122,231,255,0.95); }
.console .amb{ color: rgba(255,204,102,0.95); }
</style>
        """,
        unsafe_allow_html=True
    )

# HUD bovenaan (ziet er uit als een control panel)
def hud_header():
    s.markdown(
        """
<div class="hud-panel">
  <div class="hud-top">
    <div>
      <div class="hud-title">ZOD-78 / QUANTUM RIG SYNTHESIS</div>
      <div class="hud-sub">STABILITY: SEVERE • YEAR: 3060 • COOLANT LOOP: UNTRUSTED</div>
    </div>
    <div class="lights">
      <div class="light red"></div>
      <div class="light blue"></div>
      <div class="light green"></div>
    </div>
  </div>
</div>
        """,
        unsafe_allow_html=True
    )

# Laat een nep opstart zien
def system_boot():
    s.markdown('<div class="console">', unsafe_allow_html=True)

    logs = [
        "<span class='inf'>[INIT]</span> ZOD-78 CORE BOOTING",
        "<span class='ok'>[OK]</span>   MEMORY CHECK .... SUCCES",
        "<span class='amb'>[WARN]</span> THERMAL SENSOR .. WARN",
        "<span class='ok'>[OK]</span>   GPU MODULES .... ONLINE",
        "<span class='err'>[CRIT]</span> SYSTEM STABILITY SEVERE",
    ]
    # EINDE AI

    # Elke lijn in de log fake delay en schrijf antwoord
    for line in logs:
        fake_delay(0.05, 0.14)
        s.markdown(glitch_text(line) + "<br/>", unsafe_allow_html=True)

    s.markdown("</div>", unsafe_allow_html=True)

# console lines "streamen" zodat het lijkt alsof het live print
def streaming_console(lines):
    s.markdown('<div class="console">', unsafe_allow_html=True)
    for line in lines:
        fake_delay(0.05, 0.14)
        s.markdown(glitch_text(line) + "<br/>", unsafe_allow_html=True)
    s.markdown("</div>", unsafe_allow_html=True)

# AI-output mooier tonen
def render_ai_output_as_console(text):
    safe = (
        text.replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
            .replace("\n", "<br/>")
    )
    s.markdown(f"<div class='console'>{safe}</div>", unsafe_allow_html=True)
