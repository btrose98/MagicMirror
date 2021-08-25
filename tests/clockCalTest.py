# importing whole module
from tkinter.ttk import *
import tkinter as tk
from tkinter import *
from weatherCall import weatherCall
from newsCall import newsCall
from quickstart import quickstart
from time import strftime
 

weather = weatherCall()
news = newsCall()
calendar = quickstart()

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
    weatherWidget = Label(root, font = ('calibri', 10), text= weatherText, fg='white', bg='pink', justify=LEFT)
    weatherWidget.pack(side=TOP, anchor=E)
    #--------------END OF WEATHER--------------------
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
    masterclock.pack(side=TOP, anchor=W)
    time()
    #--------------END OF CLOCK--------------------
    #--------------CALENDAR--------------------

    weatherText = "CALENDAR\n\n EVENTS: {events}".format(events = quickstart.event)
    weatherWidget = Label(root, font = ('calibri', 10), text= weatherText, fg='white', bg='pink', justify=LEFT)
    weatherWidget.pack(side=TOP, anchor=E)

    #--------------END OF CALENDAR--------------------
    #--------------NEWS--------------------
    newsText = "NEWS\n\n 1: {title1}\n 2: {title2}\n 3: {title3}".format(title1 = news.articleTitle1, title2 = news.articleTitle2, title3 = news.articleTitle3)
    newsWidget = Label(root, font = ('calibri', 10), text=newsText, fg='white', bg='pink', justify=LEFT)
    newsWidget.pack(side=BOTTOM, anchor=E)
    #--------------END OF NEWS--------------------

    root.attributes("-fullscreen", True)
    root.configure(background='black')
    startupscreen.destroy()
    root.mainloop()

#--------------END OF MAIN SCREEN--------------------


if __name__ == main():
    main()





