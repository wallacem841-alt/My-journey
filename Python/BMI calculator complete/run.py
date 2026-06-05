import tkinter as tk
from tkinter import ttk
from UI import MainMenu, ConfigPage, CalcPage, LangPage
from utils import load_json
    
# -------------------------
# Load external config
# -------------------------

config = load_json("config.json")
lang = load_json(f"language/{config["language"]}.json")

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("BMI Calculator")
        self.geometry("300x300")
        self.state("zoomed")  # Fullscreen-like behavior
        self.configure(bg=config["theme"])

        container = tk.Frame(self)
        container.pack(fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Store all pages here
        self.frames = {}

        # List all your pages here
        for F in (MainMenu, ConfigPage, CalcPage, LangPage):
            page_name = F.__name__
            frame = F(container, self, lang)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("MainMenu")

    def show_frame(self, page_name):
            #Bring any frame to the front.
            frame = self.frames[page_name]
            frame.tkraise()

if __name__ == "__main__":
    app = App()
    app.mainloop()