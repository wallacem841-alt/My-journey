import tkinter as tk
from tkinter import messagebox
from math import ceil

'''
1. value_if_allowed: This parameter represents the value in the entry box after the latest change (key press).
2. isdigit(): This method checks if the string consists only of digits.
3. or value_if_allowed == "": This condition allows the entry to be empty, which is important when the user
deletes all the text in the entry box.
4. return True: If the input is valid (either digits or empty), the function returns True, allowing the change.
5. return False: If the input is not valid (contains non-digit characters), the function returns False,
preventing the change.
'''
def validate_entry(value_if_allowed):
    if value_if_allowed.isdigit() or value_if_allowed == "":
        return True
    else:
        return False

'''
1. on_submit function: This function is triggered when the submit button is pressed.
2. entry.get(): This retrieves the current value from the entry box.
3. if entered_value: This checks if the entry box is not empty.
4. else: If the entry box is empty, it displays a warning message box asking the user to enter a number.
'''

def on_submit():
    entered_value = entry.get()
    try:
        entered_value = int(entered_value)
    except ValueError:
        messagebox.showwarning("Input Error", "Please enter a number.")
        #this stops the code
        return
    
    #separate the entered value to calculate
    calculator = entered_value
    binary = []

    while calculator >= 1:
        i = calculator % 2
        binary.append(i)
        calculator //= 2 # the // rounds down the division
        print(i, calculator)
    
    #reverse the list
    binary.reverse()

    #turns binary into a string to make it more pleasing to the eye
    Result = ''.join(map(str, binary))

    #display a msg box with the result
    messagebox.showinfo(f"{entered_value} in binary is", Result)

root = tk.Tk()
root.title("Number Input")

'''
1. root.register(validate_entry): Registers the validate_entry function with Tkinter so it can be used
as a validation command.
2. '%P': This is a substitution parameter that represents the current value of the entry
widget after the latest change. It gets passed to the validate_entry function.
3. validate_cmd: This is a tuple that stores the validation command and its parameter,
ready to be used in the entry widget.
'''

validate_cmd = (root.register(validate_entry), '%P')

'''
1. tk.Entry(root): This creates an entry widget where users can input text.
2. validate="key": This tells Tkinter to validate the entry every time a key is pressed.
3. validatecommand=validate_cmd: This assigns the validation command (defined earlier) to the entry widget.
'''
entry = tk.Entry(root, validate="key", validatecommand=validate_cmd)
entry.grid(column=0, row=0)

'''
1. tk.Button(root, text="Submit"): This creates a button widget with the text "Submit."
2. command=on_submit: This assigns the on_submit function to be called when the button is pressed.
'''

submit_button = tk.Button(root, text="Submit", command=on_submit)
submit_button.grid(column=1, row=0)

root.mainloop()