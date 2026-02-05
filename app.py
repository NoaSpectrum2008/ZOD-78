# Importeren van streamlit ui comps en ai_engine
import streamlit as s
from ui_components import inject_theme_css, system_boot
from ai_engine import generate_build

# Basics voor streamlit
s.set_page_config(
    page_title="ZOD-78 Supercomputer",
    page_icon="🟥",
    layout="centered"
)

# Laad de opmaak
inject_theme_css()

s.title("🟥 ZOD-78 SIMULATION TERMINAL")
s.caption("STATUS: SEVERE")

# Laat het systeem aan gaan
system_boot()

# Siders en selectboxen
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

# Start simulatie
if s.button("RUN SIMULATION"):
    data = {
        "budget": budget,
        "resolution": resolution,
        "fps": fps,
        "priority": priority,
        "games": games,
    }

    with s.spinner("SIMULATION RUNNING..."):
        output = generate_build(data)

    # Toon "console achtige" output
    s.markdown("```text")
    s.write(output)
    s.markdown("```")
