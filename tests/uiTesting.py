from tkinter.ttk import *
import tkinter as tk
from tkinter import *
from weatherCall import weatherCall
from newsCall import newsCall
from quickstart import quickstart
from yahooApiCall import yahooApiCall
from time import strftime
from PIL import ImageTk,Image  
from cryptoCall import cryptoCall

weather = weatherCall()
news = newsCall()
calendar = quickstart()
yahoo = yahooApiCall()
crypto = cryptoCall()

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
    weatherContainer = Label(root, bg='black')
    weatherContainer.grid(row=0, column=1, sticky="ne")

    weatherImage = ImageTk.PhotoImage(master = weatherContainer, image = Image.open(weather.imagePath)) 
    weatherImageWidget = Label(weatherContainer, image = weatherImage)
    weatherImageWidget.grid(row=0, sticky="n")

    weatherText = "WEATHER\n\n Temperature:  {temp} \n Humidity:  {humid}".format(temp = weather.temp, humid = weather.humidity)
    weatherTextWidget = Label(weatherContainer, font = ('calibri', 10), text= weatherText, fg='white', bg='pink')
    weatherTextWidget.grid(row=1, sticky="s")

    #--------------STONKS--------------------
    stocksContainer = Label(root)
    stocksContainer.grid(row=2, columnspan=2, sticky="sew")
    stocksContainer.columnconfigure(1, weight=1)

    date = yahoo.date
    close = yahoo.closeList
    tickers = yahoo.tickers
        
    stocks = f"STOCKS\n {date}\n\nTicker: {tickers[0]}\t{tickers[1]}\t{tickers[2]}\n\t{close[0]}\t{close[1]}\t{close[2]}\n"
    stocksWidget = Label(stocksContainer, font = ('calibri', 10), text=stocks, fg='white', bg='pink')
    stocksWidget.grid(columnspan=2, sticky="ew")

    #--------------CRYPTO--------------------
    cryptoContainer = Label(root)
    cryptoContainer.grid(row=3, columnspan=2, sticky="sew")
    cryptoContainer.columnconfigure(1, weight=1)

    cryptoText = "${coin1},      ${coin2},        ${coin3}".format(coin1 = crypto.btc, coin2 = crypto.eth, coin3 = crypto.ada)
    cryptoWidget = Label(cryptoContainer, font = ('calibri', 10), text=cryptoText, fg='white', bg='pink')
    cryptoWidget.grid(columnspan=2, sticky="ew")
    
    #--------------CLOCK--------------------
    # This function is used to display time on the label
    def time():
        string = strftime('%H:%M:%S %p')
        masterclock.config(text = string)
        masterclock.after(1000, time)

    clockContainer = Label(root)
    clockContainer.grid(row=0, column=0, sticky="nw")

    masterclock = Label(clockContainer, font = ('calibri', 40, 'bold'), background = 'pink', foreground = 'white')
    masterclock.grid(sticky="nw")
    time()
 
    #--------------CALENDAR--------------------
    calendarContainer = Label(root)
    calendarContainer.grid(row=1, column=0, sticky="w")

    calendarText = "CALENDAR: \n\n {event1} \n {event2} \n {event3} \n {event4} \n {event5} \n {event6} \n {event7} \n {event8} \n {event9} \n {event10}".format(event1 = calendar.event1, event2 = calendar.event2, event3 = calendar.event3, event4 = calendar.event4, event5 = calendar.event5, event6 = calendar.event6, event7 = calendar.event7, event8 = calendar.event8, event9 = calendar.event9, event10 = calendar.event10)
    calendarWidget = Label(calendarContainer, font = ('calibri', 10), text= calendarText, fg='white', bg='pink')
    calendarWidget.grid(sticky="w")

    #--------------NEWS--------------------
    newsContainer = Label(root)
    newsContainer.grid(row=1, column=1, sticky="e")
    
    newsText = "NEWS\n\n 1: {title1}\n 2: {title2}\n 3: {title3}".format(title1 = news.articleTitle1, title2 = news.articleTitle2, title3 = news.articleTitle3)
    newsWidget = Label(newsContainer, font = ('calibri', 10), text=newsText, fg='white', bg='pink')
    newsWidget.grid(sticky="e")

    root.attributes("-fullscreen", True)
    root.configure(background='black')
    root.columnconfigure(1, weight=1)
    root.rowconfigure(1, weight=1)
    startupscreen.destroy()
    root.mainloop()

#--------------END OF MAIN SCREEN--------------------

if __name__ == main():
    main()