import tkinter as tk
from tkinter import messagebox
import csv
import pandas as pd

def sign_up_screen(parent):
    login = tk.Toplevel(parent)
    login.title('Sign up')
    login.wm_state('zoomed')
    login.configure(bg='#5c5252')

    #page logic
    def Submit():
        #reads input boxes
        submited_username = Username_entry.get()
        submited_password = password_entry.get()

        #checks if input boxes are empty
        if not submited_username or not submited_password:
            messagebox.showwarning("Input Error", "Please enter a Username and password.")
            return
        
        #Reads Dataframe and checks username avalability
        password_dataframe = pd.read_csv('Passwords.csv')

        if submited_username in password_dataframe['username'].values:
            messagebox.showwarning("Username Error", "This username is already registered!")
            return

        #compiles and register username and password
        data =[submited_username, submited_password]
        file_name = 'Passwords.csv'

        with open(file_name, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(data)

        #Closes current tab and moves back to root page
        login.destroy()
        parent.deiconify()
        parent.wm_state('zoomed')


    #Page config
    Main_label = tk.Label(login, bg='#000000', fg='#ffffff', text='Sign up', height=2, width=10, font=('Arial', 15))
    Main_label.pack(padx=0, pady=20)

    #Username label and entry
    Username_label = tk.Label(login, text='Username', bg='#ffffff', fg='#000000')
    Username_label.pack(padx=0, pady=10)

    Username_entry = tk.Entry(login)
    Username_entry.pack(padx=0, pady=0)

    #space
    space = tk.Label(login, bg='#5c5252')
    space.pack(padx=0, pady=20)

    #password label and entry
    password_label = tk.Label(login, text='Password', bg='#ffffff', fg='#000000')
    password_label.pack(padx=0, pady=10)

    password_entry = tk.Entry(login)
    password_entry.pack(padx=0, pady=0)

    submit_button = tk.Button(login, text='Submit', height=2, width=10, font=('Arial', 24),
                              command=Submit, bg='#1941e3', fg='#ffffff')
    submit_button.pack(padx=20, pady=20)