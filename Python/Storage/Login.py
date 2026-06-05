import tkinter as tk
from tkinter import messagebox
import pandas as pd

def login_screen(parent):
    login = tk.Toplevel(parent)
    login.title('Login')
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

        #converts data to string
        submited_username = str(submited_username)
        submited_password = str(submited_password)

        #Reads Dataframe and checks if username is in dataframe
        password_dataframe = pd.read_csv('Passwords.csv')

        if submited_username not in password_dataframe['username'].values:
            messagebox.showwarning("Username Error", "This username is not registered!")
            return

        #seaches for password and checks if it's correct
        password_index = password_dataframe[password_dataframe['username'] == submited_username].index

        stored_password = password_dataframe.iloc[password_index, 1].values

        if submited_password not in stored_password:
            messagebox.showwarning("Password Error", "Password is wrong")
            return
        
        #User logged in
        messagebox.showinfo('Login info', "You've successfully logged in")

        #Closes current tab and moves back to root page
        login.destroy()
        parent.deiconify()
        parent.wm_state('zoomed')


    #Page config
    Main_label = tk.Label(login, bg='#b31614', fg='#ffffff', text='Login', height=2, width=10, font=('Arial', 15))
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