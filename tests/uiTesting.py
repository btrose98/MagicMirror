# https://www.youtube.com/watch?v=YXPyB4XeYLA

from tkinter import *

root = Tk()
root.title('Smart Mirror - User Interface')
root.configure(background='black')

# labelWidget1 = Label(root, text="Calendar", fg='white', bg='black').grid(row=0, column=0)

# labelWidget2 = Label(root, text="Weather", fg='white', bg='black').grid(row=0, column=1)

# labelWidget3 = Label(root, text="Stonks", fg='white', bg='black').grid(row=1, column=0)

labelWidget1 = Label(root, text="Calendar", fg='white', bg='black')
labelWidget1.pack(side=TOP, anchor=NW)

labelWidget2 = Label(root, text="Weather", fg='white', bg='black')
labelWidget2.pack(side=TOP, anchor=NE)

labelWidget3 = Label(root, text="Stonks", fg='white', bg='black')
labelWidget3.pack(side=BOTTOM, anchor=SW)

root.mainloop()