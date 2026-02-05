# Importeren van current time etc
import time
# Importeren van random
import random

# Wacht een klein random moment tussen 
def fake_delay(min_s=0.25, max_s=0.65):
    time.sleep(random.uniform(min_s, max_s))

# Vervangt soms een teken door een "glitch"-symbool
def glitch_text(text):
    symbols = ["#", "@", "%", "&", "*", "!", "~"]
    result = []

    # Voor characters uit de tekst als teken niet leeg is een random getal voor 0.035 sec
    for char in text:
        if char != " " and random.random() < 0.035:
            result.append(random.choice(symbols))
        else:
            result.append(char)

    return "".join(result)
