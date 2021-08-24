# https://www.youtube.com/watch?v=YXPyB4XeYLA

from tkinter import *
from weatherCall import weatherCall
from newsCall import newsCall

root = Tk()
root.title('Smart Mirror - User Interface')
root.configure(background='black')

#--------------Calendar--------------------
labelWidget1 = Label(root, text="Calendar", fg='white', bg='black')
labelWidget1.pack(side=TOP, anchor=W)

#--------------Weather--------------------
weather = weatherCall()
temperature = weather.temp
humidity = weather.humidity
weatherText = "WEATHER\n\n Temperature:  {temp} \n Humidity:  {humid}".format(temp = temperature, humid = humidity)
labelWidget2 = Label(root, text= weatherText, fg='white', bg='black')
labelWidget2.pack(side=TOP, anchor=E)

#--------------Stonks--------------------
labelWidget3 = Label(root, text="Stonks", fg='white', bg='black')
labelWidget3.pack(side=BOTTOM, anchor=W)
yahoo = yahooApiCall()
date = yahoo.date
open = yahoo.openList
close = yahoo.closeList
    
stocks = "STOCKS\n {d}\n\nTicker:  {t1} \t {t2} \t {t3} \nOpen: {o1} \t {o2} \t {o3} \nClose: {c1} \t {c2} \t {c3} \n ".format(t1=tickers[0], t2=tickers[1], t3=tickers[2], d=date, o1=open[0], o2=open[1], o3=open[2], c1=close[0], c2=close[1], c3=close[2])

#--------------News--------------------
newsText = "NEWS\n 1:   {title1}\n 2:   {title2}\n 3:   {title3}".format(title1 = newsCall.articleTitle1, title2 = newsCall.articleTitle2, title3 = newsCall.articleTitle3)
labelWidget4 = Label(root, text=newsText, fg='white', bg='black')
labelWidget4.pack(side=BOTTOM, anchor=E)

root.mainloop()