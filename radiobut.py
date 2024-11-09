from tkinter import *
window = Tk()
window.title('Radio Button')
choice = IntVar()
choice.set("1")
def clicked(value):
    myLabel = Label(window,text=value)
    myLabel.pack()
    print(value)

Radiobutton(window, text="Male",variable=choice,value=1,command=lambda:clicked(choice.get())).pack(anchor=W)
Radiobutton(window, text="Female",variable=choice,value=2,command=lambda:clicked(choice.get())).pack(anchor=W)
