import json

# -------------------------
# Helper functions
# -------------------------

def load_json(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
    
def change_color(color):
    config = load_json("config.json")
    config["theme"] = color
    with open("config.json", "w", encoding="utf-8") as f:
        json.dump(config, f, indent=4, ensure_ascii=False)

def change_lang(lang):
    config = load_json("config.json")
    config["language"] = lang
    with open("config.json", "w", encoding="utf-8") as f:
        json.dump(config, f, indent=4, ensure_ascii=False)

#--------
#data
#--------

LANG_TABLE = [
    ("en", "English"),
    ("pt", "Português"),
    ("es", "Español"),
    ("ja", "日本語"),
    ("fr", "Français"),
    ("la", "Latina"),
    ("ko", "한국어")
]