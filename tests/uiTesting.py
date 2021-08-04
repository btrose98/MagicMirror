# https://www.youtube.com/watch?v=YXPyB4XeYLA

from tkinter import *
from weatherCall import weatherCall

root = Tk()
root.title('Smart Mirror - User Interface')
root.configure(background='black')

weather = weatherCall()
temperature = weather.temp
humidity = weather.humidity

labelWidget1 = Label(root, text="Calendar", fg='white', bg='black')
labelWidget1.pack(side=TOP, anchor=W)

weatherText = "WEATHER\n\n Temperature:  {temp} \n Humidity:  {humid}".format(temp = temperature, humid = humidity)
labelWidget2 = Label(root, text= weatherText, fg='white', bg='black')
labelWidget2.pack(side=TOP, anchor=E)

labelWidget3 = Label(root, text="Stonks", fg='white', bg='black')
labelWidget3.pack(side=BOTTOM, anchor=W)

root.mainloop()