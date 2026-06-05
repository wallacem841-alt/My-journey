import tkinter

root = tkinter.Tk()

mylabel1 = tkinter.Label(root, text='hello, world')#.grid(row=0, column=0) # this is another way to do it
mylabel2 = tkinter.Label(root, text='Shenhe is the best wifu')#.grid(row=1, column=1)

mylabel1.grid(row=0, column=0)
mylabel2.grid(row=1, column=1)

root.mainloop()