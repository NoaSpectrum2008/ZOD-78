# Streamlit en utilities van utils.py importeren
import streamlit as s
from utils import fake_delay, glitch_text

# CSS voor de supercomputer look
def inject_theme_css():
    s.markdown("""
    <style>
    body { background-color: #05060a; color: #c7ffd9; }
    </style>
    """, unsafe_allow_html=True)

# Laat een nep opstart zien
def system_boot():
    s.markdown("```text")

    logs = [
        "ZOD-78 CORE BOOTING",
        "MEMORY CHECK .... SUCCES",
        "THERMAL SENSOR .. WARN",
        "GPU MODULES .... ONLINE",
        "SYSTEM STABILITY SEVERE",
    ]

    # Elke lijn in de log fake delay en schrijf antwoord
    for line in logs:
        fake_delay()
        s.write(glitch_text(line))

    s.markdown("```")
