from tkinter.ttk import *
import tkinter as tk
from tkinter import *
from weatherCall import weatherCall
from newsCall import newsCall
from quickstart import quickstart
from yahooApiCall import yahooApiCall
from time import strftime

weather = weatherCall()
news = newsCall()
calendar = quickstart()
yahoo = yahooApiCall()

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
    weatherWidget = Label(root, font = ('calibri', 10), text= weatherText, fg='white', bg='pink')
    weatherWidget.grid(row=0, column=1, sticky="e")
    
    #--------------STONKS--------------------
    date = yahoo.date
    close = yahoo.closeList
    tickers = yahoo.tickers
        
    stocks = f"STOCKS\n {date}\n\nTicker: {tickers[0]}\t{tickers[1]}\t{tickers[2]}\n\t{close[0]}\t{close[1]}\t{close[2]}\n"
    stocksWidget = Label(root, font = ('calibri', 10), text=stocks, fg='white', bg='pink')
    stocksWidget.grid(row=2, column=0, columnspan=2, sticky="sew")
    
    #--------------CLOCK--------------------
    # This function is used to
    # display time on the label
    def time():
        string = strftime('%H:%M:%S %p')
        masterclock.config(text = string)
        masterclock.after(1000, time)
    # Styling the label widget so that clock
    # will look more attractive
    masterclock = Label(root, font = ('calibri', 40, 'bold'), background = 'pink', foreground = 'white')
    # Placing clock at the centre
    # of the tkinter window
    masterclock.grid(row=0, column=0, sticky="w")
    time()
 
    #--------------CALENDAR--------------------
    calendarText = "CALENDAR: \n\n {event1} \n {event2} \n {event3} \n {event4} \n {event5} \n {event6} \n {event7} \n {event8} \n {event9} \n {event10}".format(event1 = calendar.event1, event2 = calendar.event2, event3 = calendar.event3, event4 = calendar.event4, event5 = calendar.event5, event6 = calendar.event6, event7 = calendar.event7, event8 = calendar.event8, event9 = calendar.event9, event10 = calendar.event10)
    calendarWidget = Label(root, font = ('calibri', 10), text= calendarText, fg='white', bg='pink')
    calendarWidget.grid(row=1, column=0, sticky="w")

    #--------------NEWS--------------------
    newsText = "NEWS\n\n 1: {title1}\n 2: {title2}\n 3: {title3}".format(title1 = news.articleTitle1, title2 = news.articleTitle2, title3 = news.articleTitle3)
    newsWidget = Label(root, font = ('calibri', 10), text=newsText, fg='white', bg='pink')
    newsWidget.grid(row=1, column=1, sticky="e")

    root.attributes("-fullscreen", True)
    root.configure(background='black')
    root.columnconfigure(1, weight=1)
    root.rowconfigure(1, weight=1)
    startupscreen.destroy()
    root.mainloop()

#--------------END OF MAIN SCREEN--------------------

if __name__ == main():
    main()