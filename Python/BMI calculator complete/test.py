from utils import load_json

config = load_json("config.json")
lang = load_json(f"language/{config["language"]}.json")

for index, color_names in lang["colors"].items():
    print(index, color_names)