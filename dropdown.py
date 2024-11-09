from tkinter import*
window=Tk()
window.title('Drop down menu')
clicked=StringVar()
options=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
clicked.set(options[1])
def show():
    myLabel = Label(window, text=clicked.get()).grid(row=2,column=0)

drop = OptionMenu(window, clicked, *options)
drop.grid(row=0,column=0)

myButton= Button(window, text="Show Selection", command=show).grid(row=1,column=0)
