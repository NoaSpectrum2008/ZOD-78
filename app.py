# Importeren van streamlit ui comps en ai_engine
import streamlit as s
from ui_components import inject_theme_css, hud_header, system_boot, streaming_console, render_ai_output_as_console
from ai_engine import generate_build

# Basics voor streamlit
s.set_page_config(
    page_title="ZOD-78 Supercomputer",
    page_icon="🟥",
    layout="centered"
)

# Laad de opmaak
inject_theme_css()

hud_header()

s.title("🟥 ZOD-78 SIMULATION TERMINAL")
s.caption("STATUS: SEVERE • OPERATOR ACCESS: LIMITED • YEAR: 3060")

# Laat het systeem "aan gaan"
system_boot()

# Opmaal
with s.sidebar:
    budget = s.slider("Budget (€)", 500, 3000, 1200, 50)
    resolution = s.selectbox("Resolutie", ["1080p", "1440p", "4K"])
    fps = s.selectbox("FPS target", ["60", "120", "144", "240"])
    priority = s.selectbox(
        "Prioriteit",
        ["Max FPS", "Stil", "Prijs/Kwaliteit", "Toekomstbestendig"]
    )

# Games tests
games = s.multiselect(
    "Games",
    ["War Thunder", "CS2", "Fortnite", "Warzone", "Cyberpunk 2077"],
    default=["War Thunder"]
)

# Control panel knoppen (voelt als echte machine knoppen)
c1, c2, c3, c4 = s.columns(4)


with c3:
    run = s.button("RUN SIM")
with c4:
    abort = s.button("ABORT")

if abort:
    streaming_console([
        "<span class='err'>[ABORT]</span> OPERATOR INTERRUPT RECEIVED",
        "<span class='amb'>[WARN]</span> COOLANT LOOP STABILIZING…",
        "<span class='ok'>[OK]</span>   CORE TEMPERATURE DROPPING",
    ])
    s.stop()



# Start simulatie
if run:
    if not games:
        streaming_console(["<span class='err'>[CRIT]</span> NO WORKLOAD SELECTED"])
        s.stop()

    streaming_console([
        "<span class='inf'>[SIM]</span>  BUILD MATRIX: CONSTRUCT",
        "<span class='inf'>[SIM]</span>  GPU/CPU BALANCE: SOLVING",
        "<span class='amb'>[WARN]</span> OPERATOR EXPECTATIONS: HIGH",
        "<span class='err'>[CRIT]</span> STABILITY WINDOW: NARROW",
        "<span class='ok'>[OK]</span>   OUTPUT CHANNEL: READY",
    ])

    data = {
        "budget": budget,
        "resolution": resolution,
        "fps": fps,
        "priority": priority,
        "games": games,
    }

    with s.spinner("SIMULATION RUNNING..."):
        output = generate_build(data)

    # Toon "console achtige" output (mooier)
    s.subheader("OUTPUT / TELEMETRY DUMP")
    render_ai_output_as_console(output)
