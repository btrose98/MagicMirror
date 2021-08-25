# https://www.youtube.com/watch?v=YXPyB4XeYLA
import tkinter as tk
from tkinter import *
from weatherCall import weatherCall
from newsCall import newsCall
import time

weather = weatherCall()
news = newsCall()


def main():

#--------------STARTUP SCREEN--------------------

    #create a spash screen
    startupscreen = tk.Tk()
    startupscreen.title('Smart Mirror: Python Mod')
    startupscreen.configure(background='black')
    startupscreen.overrideredirect(True) # remove ability to close application 

    #set parameters for display
    welcometext = Label(startupscreen, font = ('caviar dreams', 40), bg='black', fg='white')
    welcometext.config(text='Mirror: Smart Living')
    welcometext.pack(side=LEFT, padx= 120, pady=80)

    # Gets the requested values of the height and widht.
    windowWidth = startupscreen.winfo_reqwidth()
    windowHeight = startupscreen.winfo_reqheight()

    # Gets both half the screen width/height and window width/height
    positionRight = int(startupscreen.winfo_screenwidth()/2.7 - windowWidth/2)
    positionDown = int(startupscreen.winfo_screenheight()/2 - windowHeight/2)

    # Positions the window in the center of the page.
    startupscreen.geometry("+{}+{}".format(positionRight, positionDown))
    startupscreen.update()

#--------------END OF STARTUP SCREEN--------------------

#--------------START OF MAIN SCREEN--------------------

    root = tk.Tk()
    root.title('Mirror')

    #--------------WEATHER--------------------
    weatherText = "WEATHER\n\n Temperature:  {temp} \n Humidity:  {humid}".format(temp = weather.temp, humid = weather.humidity)
    weatherWidget = Label(root, font = ('caviar dreams', 10), text= weatherText, fg='white', bg='pink', justify=LEFT)
    weatherWidget.pack(side=TOP, anchor=E)
    #--------------END OF WEATHER--------------------

    #--------------NEWS--------------------
    newsText = "NEWS\n\n 1: {title1}\n 2: {title2}\n 3: {title3}".format(title1 = news.articleTitle1, title2 = news.articleTitle2, title3 = news.articleTitle3)
    newsWidget = Label(root, font = ('caviar dreams', 10), text=newsText, fg='white', bg='pink', justify=LEFT)
    newsWidget.pack(side=BOTTOM, anchor=E)
    #--------------END OF NEWS--------------------

    #--------------CLOCK--------------------
    while True:
        #get the hour 
        def getHour(time1=''):
            time2 = time.strftime("%H")
            if time2 != time1:
                time1 = time2
                clock_frame.config(text=time2)
            clock_frame.after(200, getHour)

        #get the minutes and seconds
        def getMinSec(time3=''):
            time4 = time.strftime(":%M:%S")
            if time4 != time3:
                time3 = time4
                clock_frame2.config(text=time4)
            clock_frame2.after(200, getMinSec)      

        masterclock = Label(root)
        masterclock.pack(side=TOP, anchor=W, padx=45)
        
        #masterclock.configure(background='black')
        clock_frame = Label(root, font = ('caviar dreams', 130), bg='black', fg='white')
        clock_frame.pack(in_=masterclock, side=LEFT)
        clock_frame2 = Label(root, font = ('caviar dreams', 70), bg='black', fg='white')
        clock_frame2.pack(in_=masterclock, side=LEFT, anchor = NW, ipady=15)

        getHour()
        getMinSec()
    #--------------END OF CLOCK--------------------


        root.attributes("-fullscreen", True)
        root.configure(background='black')
        startupscreen.destroy()
        root.mainloop()

#--------------END OF MAIN SCREEN--------------------


if __name__ == main():
    main()

# root = Tk()
# root.title('Smart Mirror - User Interface')
# root.configure(background='black')

# #--------------Calendar--------------------
# labelWidget1 = Label(root, text="Calendar", fg='white', bg='black')
# labelWidget1.pack(side=LEFT, anchor=W)



# #--------------Stonks--------------------
# labelWidget3 = Label(root, text="Stonks", fg='white', bg='black')
# labelWidget3.pack(side=BOTTOM, anchor=W)


# root.mainloop()


#=======
from yahooApiCall import yahooApiCall



#=======
#--------------Weather--------------------
weather = weatherCall()
temperature = weather.temp
humidity = weather.humidity
weatherText = "WEATHER\n\n Temperature:  {temp} \n Humidity:  {humid}".format(temp = temperature, humid = humidity)
labelWidget2 = Label(root, text= weatherText, fg='white', bg='black')
labelWidget2.pack(side=TOP, anchor=E)

#--------------Stonks--------------------
yahoo = yahooApiCall()
date = yahoo.date
close = yahoo.closeList
tickers = yahoo.tickers
    
stocks = f"STOCKS\n {date}\n\nTicker: {tickers[0]}\t{tickers[1]}\t{tickers[2]}\n\t{close[0]}\t{close[1]}\t{close[2]}\n"
labelWidget3 = Label(root, text=stocks, fg='white', bg='black')
labelWidget3.pack(side=BOTTOM, anchor=W)
#--------------News--------------------
newsText = "NEWS\n 1:   {title1}\n 2:   {title2}\n 3:   {title3}".format(title1 = newsCall.articleTitle1, title2 = newsCall.articleTitle2, title3 = newsCall.articleTitle3)
labelWidget4 = Label(root, text=newsText, fg='white', bg='black')
labelWidget4.pack(side=BOTTOM, anchor=E)

root.mainloop()

