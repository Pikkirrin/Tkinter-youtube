from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("radio buttons")
root.iconbitmap("Head.ico")

r = IntVar()
r.set(2)

Radiobutton(root, text="Option 1", variable=r, value=1).pack()
Radiobutton(root, text="Option 2", variable=r, value=2).pack()

myLabel = Label(root, text=r.get())
myLabel.pack()

root.mainloop()
