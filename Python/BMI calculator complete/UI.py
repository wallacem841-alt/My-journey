import tkinter as tk
from utils import load_json, change_color, LANG_TABLE, change_lang
from tkinter import ttk
from Calculator_bk import number_treatment, bmi_category

config = load_json("config.json")

class MainMenu(tk.Frame):
    def __init__(self, master, controller, lang):
        super().__init__(master)

        self.configure(bg=config["theme"])

        # Make this frame responsive
        self.grid_rowconfigure(0, weight=1)   # top empty space
        self.grid_rowconfigure(1, weight=5)   # buttons area
        self.grid_rowconfigure(2, weight=1)   # bottom empty space
        self.grid_columnconfigure(0, weight=1)

        # Text
        btn_calc_text = lang["buttons"]["calc"]
        btn_config_text = lang["buttons"]["config"]
        btn_lang_text = lang["buttons"]["language"]

        # Create a sub-frame to center buttons
        button_area = tk.Frame(self, bg=config["theme"])
        button_area.grid(row=1, column=0, sticky="nsew")

        # Make button area responsive
        button_area.grid_columnconfigure(0, weight=1)
        button_area.grid_rowconfigure(0, weight=1)
        button_area.grid_rowconfigure(1, weight=1)
        button_area.grid_rowconfigure(2, weight=1)
        button_area.grid_rowconfigure(3, weight=1)
        button_area.grid_rowconfigure(4, weight=1)

        # ---- BUTTONS ----
        button_calc = ttk.Button(button_area, text=btn_calc_text,
                                 command=lambda: controller.show_frame("CalcPage"))
        button_calc.grid(row=0, column=0, sticky="ewsn")

        button_config = ttk.Button(button_area, text=btn_config_text,
                                   command=lambda: controller.show_frame("ConfigPage"))
        button_config.grid(row=2, column=0, sticky="ewsn")

        button_lang = ttk.Button(button_area, text=btn_lang_text,
                                   command=lambda: controller.show_frame("LangPage"))
        button_lang.grid(row=4, column=0, sticky="ewsn")

class ConfigPage(tk.Frame):
    def __init__(self, master, controller, lang):
        super().__init__(master)

        btn_back_text = lang["buttons"]["back"]
        label_warning_text = lang["warnings"]["color_change"]

        self.configure(bg=config["theme"])

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=5)
        self.grid_columnconfigure(0, weight=1)

        button_area = tk.Frame(self, bg=config["theme"])
        button_area.grid(row=1, column=0, sticky="nsew")

        button_area.grid_columnconfigure(0, weight=1)
        
        temp = 0
        for index, color_names in lang["colors"].items():
            button_area.grid_rowconfigure(temp, weight=1)
            button_temp = ttk.Button(button_area, text=color_names,
                                     command=lambda color=index: change_color(color))
            button_temp.grid(row=temp, column=0, sticky="ewsn")
            temp += 1
            button_area.grid_rowconfigure(temp, weight=1)
            temp += 1

        top_area = tk.Frame(self, bg=config["theme"])
        top_area.grid(row=0, column=0, sticky="nsew")

        top_area.grid_columnconfigure(0, weight=1)
        top_area.grid_columnconfigure(1, weight=4)

        top_area_back = ttk.Button(top_area, text=btn_back_text,
                                   command=lambda: controller.show_frame("MainMenu"))
        top_area_back.grid(row=0, column=0, sticky="ewsn")

        top_area_label = ttk.Label(top_area, text=label_warning_text)
        top_area_label.grid(row=0, column=1, sticky="ewsn")

class CalcPage(tk.Frame):
    def __init__(self, master, controller, lang):
        super().__init__(master)

        #--------
        #text
        #--------

        btn_back_text = lang["buttons"]["back"]
        Label_weight_text= lang["warnings"]["weight_text"]
        Label_height_text = lang["warnings"]["height_text"]
        btn_calc_text = lang["buttons"]["calc"]
        Label_result_text_initial = lang["results"]["initial"]
        Label_result_text_nan = lang["results"]["nan"]
        Label_result_text_0_division = lang["results"]["zero"]
        Label_result_text_negative = lang["results"]["negative"]
        Label_after_result_text = lang["results"]["after_result_text"]


        #--------
        #alpha frame
        #--------

        self.configure(bg=config["theme"])

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)
        self.grid_rowconfigure(5, weight=1)
        self.grid_columnconfigure(0, weight=1)

        #--------
        #grid 0
        #--------

        top_area = tk.Frame(self, bg=config["theme"])
        top_area.grid(row=0, column=0, sticky="nsew")

        top_area.grid_columnconfigure(0, weight=1)
        top_area.grid_columnconfigure(1, weight=4)

        top_area_back = ttk.Button(top_area, text=btn_back_text,
                                   command=lambda: controller.show_frame("MainMenu"))
        top_area_back.grid(row=0, column=0, sticky="ewsn")

        #--------
        #grid 1
        #--------

        input_area = tk.Frame(self, bg=config["theme"])
        input_area.grid(row=1, column=0, sticky="nsew")

        input_area.grid_columnconfigure(0, weight=1)
        input_area.grid_columnconfigure(1, weight=1)
        input_area.grid_rowconfigure(0, weight=1)
        input_area.grid_rowconfigure(1, weight=1)
        input_area.grid_rowconfigure(2, weight=1)

        weight_input_box = ttk.Spinbox(input_area, from_=0, to=1000)
        weight_input_box.grid(row=0, column=0, sticky="nsew")

        weight_input_text = ttk.Label(input_area, text=Label_weight_text)
        weight_input_text.grid(row=0, column=1, sticky="news")

        height_input_box = ttk.Spinbox(input_area, from_=0, to=1000)
        height_input_box.grid(row=2, column=0, sticky="nsew")

        height_input_text = ttk.Label(input_area, text=Label_height_text)
        height_input_text.grid(row=2, column=1, sticky="news")

        #--------
        #grid 2
        #--------

        button_calc_area = tk.Frame(self, bg=config["theme"])
        button_calc_area.grid(row=2, sticky="news")

        button_calc_area.grid_columnconfigure(0, weight=3)
        button_calc_area.grid_columnconfigure(1, weight=1)

        calc_button = ttk.Button(button_calc_area, text=btn_calc_text,
                                 command=lambda: calc_logic())
        calc_button.grid(column=1, sticky="news")

        #--------
        #grid 4
        #--------

        result_area = tk.Frame(self, bg=config["theme"])
        result_area.grid(row=4, sticky="news")

        result_area.grid_columnconfigure(0, weight=1)
        result_area.grid_rowconfigure(0, weight=1)

        result_text = ttk.Label(result_area, text=Label_result_text_initial)
        result_text.grid(row=0, column=0, sticky="news")

        #--------
        #calc logic
        #--------

        def calc_logic():
            height_input = height_input_box.get()
            weight_input = weight_input_box.get()

            result = number_treatment(weight_input=weight_input, height_input=height_input)

            if result == "nan":
                result_text.config(text=Label_result_text_nan)
            elif result == "0_division":
                result_text.config(text=Label_result_text_0_division)
            elif result < 0:
                result_text.config(text=Label_result_text_negative)
            else:
                bmi_result = bmi_category(result)
                result_text.config(text=Label_after_result_text + f"{result:.2f}" + " ;" + lang["results"][bmi_result])

class LangPage(tk.Frame):
    def __init__(self, master, controller, lang):
        super().__init__(master)

        btn_back_text = lang["buttons"]["back"]
        label_warning_text = lang["warnings"]["color_change"]

        self.configure(bg=config["theme"])

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=5)
        self.grid_columnconfigure(0, weight=1)

        button_area = tk.Frame(self, bg=config["theme"])
        button_area.grid(row=1, column=0, sticky="nsew")

        button_area.grid_columnconfigure(0, weight=1)

        temp = 0
        for index, lang_names in LANG_TABLE:
            button_area.grid_rowconfigure(temp, weight=1)
            button_temp = ttk.Button(button_area, text=lang_names,
                                     command=lambda lang_index=index: change_lang(lang_index))
            button_temp.grid(row=temp, column=0, sticky="ewsn")
            temp += 1
            button_area.grid_rowconfigure(temp, weight=1)
            temp += 1

        top_area = tk.Frame(self, bg=config["theme"])
        top_area.grid(row=0, column=0, sticky="nsew")

        top_area.grid_columnconfigure(0, weight=1)
        top_area.grid_columnconfigure(1, weight=4)

        top_area_back = ttk.Button(top_area, text=btn_back_text,
                                   command=lambda: controller.show_frame("MainMenu"))
        top_area_back.grid(row=0, column=0, sticky="ewsn")

        top_area_label = ttk.Label(top_area, text=label_warning_text)
        top_area_label.grid(row=0, column=1, sticky="ewsn")