from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("New windows")


def open():
    global my_img
    top = Toplevel()
    top.title("2nd Window")
    my_img = ImageTk.PhotoImage(Image.open("images/Iphone_1.png"))
    my_label = Label(top, image=my_img)
    my_label.pack()
    button2 = Button(top, text='quit', command=top.destroy)
    button2.pack()


button = Button(root, text="Open second win", command=open)
button.pack()

root.mainloop()
