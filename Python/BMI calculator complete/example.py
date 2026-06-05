import json
import tkinter as tk

# --------- JSON LOADING ---------
def load_json(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

config = load_json("config.json")
lang = load_json(f"language/{config['language']}.json")

# --------- TKINTER APP ---------
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("300x300")

# background color from config
root.configure(bg=config["theme"])

# --------- BUTTON TEXT ---------
btn_calc_text = lang["buttons"]["calc"]
btn_config_text = lang["buttons"]["config"]
btn_lang_text = lang["buttons"]["language"]

# --------- UI LAYOUT ---------
button_calc = tk.Button(root, text=btn_calc_text, width=20)
button_calc.pack(pady=10)

button_config = tk.Button(root, text=btn_config_text, width=20)
button_config.pack(pady=10)

button_lang = tk.Button(root, text=btn_lang_text, width=20)
button_lang.pack(pady=10)

root.mainloop()
