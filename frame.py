from tkinter import *

root = Tk()
root.title("Frames")
root.iconbitmap('Head.ico')

frame = LabelFrame(root, padx=5, pady=5)
frame.pack(padx=5, pady=5)

b = Button(frame, text="Don't click here")
b.grid(row=0, column=0)

b2 = Button(frame, text="...or here!")
b2.grid(row=1, column=0)

root.mainloop()
