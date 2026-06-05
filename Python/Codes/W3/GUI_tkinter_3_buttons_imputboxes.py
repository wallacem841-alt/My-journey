import tkinter

def myclick():
    label1 = tkinter.Label(root, text='Shenhe best wifu', fg='blue', bg='yellow')
    label1.grid(row=0, column=1)
    #label1.pack()

def myclick2():
    label1 = tkinter.Label(root, text=e.get()+". You're worthy of shenhe", fg='blue', bg='yellow')
    label1.grid(row=1, column=1)
    #label1.pack()

root = tkinter.Tk()

mybutton = tkinter.Button(root, text='click me!', padx=50, pady=50, command=myclick, fg='red', bg='black')
# remember to no put it like this myclick() otherwise it runs the function and doesn't store it in the button

mybutton.grid(row=0, column=0)
#mybutton.pack()

e = tkinter.Entry(root, width=50, bg='#00bfff', fg='black', border=5)
e.grid(row=2, column=0)

mybutton2 = tkinter.Button(root, text='Enter your name', command=myclick2, fg='red', bg='black')
# remember to no put it like this myclick() otherwise it runs the function and doesn't store it in the button

mybutton2.grid(row=1, column=0)
#mybutton.pack()

root.mainloop()