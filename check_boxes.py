from tkinter import *

root = Tk()
root.title("check Boxes")
root.iconbitmap("Head.ico")
root.geometry("400x400")


def show():
    myLabel = Label(root, text=var.get())
    myLabel.pack()


var = StringVar()

c = Checkbutton(root, text="Check this box!", variable=var, onvalue="On", offvalue="Off")
c.deselect()
c.pack()

my_button = Button(root, text="Show selection", command=show)
my_button.pack()

root.mainloop()
