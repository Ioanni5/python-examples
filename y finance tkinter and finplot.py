import yfinance
import pandas as pd
from tkinter import *
import finplot as fplt


# create a list to store the tickers
myList = ['ES=F', 'NQ=F']
fileNames = []

# pass the list to download function in a loop and save to individual files
for name in myList:
    df = yfinance.download(name, start='2019-01-01' )
    fileName = name + '.csv'
    df.to_csv(fileName)
    fileNames.append(fileName)


# create the main window
root = Tk()

# pass the list into the listbox
var = StringVar(value=myList)
listbox1 = Listbox(root, listvariable = var, width=10, height = 5)
listbox1.grid(row=1, column=0)
    

def drawChart():
    index = listbox1.curselection()[0]
    print(index)

    df = pd.read_csv(fileNames[index], index_col='Date', parse_dates=True )

    fplt.candlestick_ochl(df[['Open', 'Close', 'High', 'Low']]) 

    pass

class Window:

    def __init__(self, root, title, geometry, message):
        self.root = root
        self.root.title(title)
        self.root.geometry(geometry) # input, size x size
        Label(self.root, text=message).grid(row=0, column=0)
        self.root.mainloop()
        pass

    pass

# create a button
button1 = Button(root, text='Draw Chart', command = drawChart)
button1.grid(row = 5, column=0)

# create the window object
window1 = Window(root, 'My new Window', '300x300', 'Select Ticker')
    


