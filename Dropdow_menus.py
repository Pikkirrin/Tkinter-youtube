from tkinter import *

root = Tk()
root.title("check Boxes")
root.iconbitmap("Head.ico")
root.geometry("400x400")


def show():
    mylabel = Label(root, text=clicked.get())
    mylabel.pack()


# Texto predeterminado
clicked = StringVar()
clicked.set("Monday")

# Drop down box
drop = OptionMenu(root, clicked, "Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
drop.pack()

mybutton = Button(root, text="Show Selection", command=show)
mybutton.pack()

root.mainloop()
