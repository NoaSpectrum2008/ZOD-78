# OS voor stabiliteit op alle platformen
import os
import cohere
from prompts import build_prompt

def get_client():
    api_key = os.getenv("COHERE_API_KEY", "").strip()
    if not api_key:
        raise RuntimeError("COHERE_API_KEY ontbreekt (Streamlit Secrets of lokaal env var).")
    return cohere.Client(api_key)

def generate_build(data):
    client = get_client()
    prompt = build_prompt(data)

    # Gebruik "live" model IDs (command en command-r alias zijn deprecated)
    model_candidates = [
        "command-r-08-2024",
        "command-a-03-2025",
    ]

    last_error = None
    for model_name in model_candidates:
        try:
            resp = client.chat(
                model=model_name,
                message=prompt,
                temperature=0.55,
            )
            return resp.text
        except Exception as e:
            last_error = e

    # Als geen enkel model werkt, geef de laatste fout door
    raise RuntimeError(f"Cohere model call failed. Last error: {last_error}")
