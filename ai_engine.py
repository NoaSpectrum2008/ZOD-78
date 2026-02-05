# Os voor overal stabiel te werken
import os
# Import AI 
import cohere
# Prompt builder importen
from prompts import build_prompt

# Haalt de Cohere API client op
def get_client():
    api_key = os.getenv("COHERE_API_KEY")

    if not api_key:
        raise RuntimeError("COHERE_API_KEY ontbreekt")

    return cohere.Client(api_key)

# Stuur data naar Cohere en ontvang het antwoord
def generate_build(data):
    client = get_client()
    prompt = build_prompt(data)

    response = client.chat(
        model="command-r",
        message=prompt,
        temperature=0.55,
    )

    return response.text
