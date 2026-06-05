import tkinter as tk
from Login import login_screen
from Sign_up import sign_up_screen

#go to login screen
def login():
    root.withdraw()
    login_screen(root)

def sign_up():
    root.withdraw()
    sign_up_screen(root)

#Creates and config the main window
root = tk.Tk()
root.title('Login/Sign up')
root.wm_state('zoomed')
root.configure(bg='#5c5252')

#Creates and config the login button
login_button = tk.Button(root, text='Login', height=2, width=10, font=('Arial', 24), 
                         bg='#b31614', fg='#ffffff', command=login)
login_button.pack(padx=300, pady=20, side='left')

#Creates and config the sigh up button
sign_up_button = tk.Button(root, text="Sign up", height=2, width=10, font=('Arial', 24),
                           bg='#000000', fg='#ffffff', command=sign_up)
sign_up_button.pack(padx=20, pady=20, side='left')

#runs main loop
root.mainloop()