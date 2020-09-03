from tkinter import *

root = Tk()
root.geometry("200x200")

e = Entry(root, width=20)
e.pack()
e.insert(0, "Enter your name:")


def myClick():
    hello = "Hello " + e.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()


myButton = Button(root, text="Enter your Name", command=myClick)
myButton.pack()

root.mainloop()
