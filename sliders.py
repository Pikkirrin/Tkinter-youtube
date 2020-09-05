from tkinter import *

root = Tk()
root.title("sliders")
root.iconbitmap('Head.ico/Users/VictorHGH/Documents/Programación/Tkinter-youtube/Head.ico')
root.geometry("400x400")

vertical = Scale(root, from_=200, to=700)
vertical.pack()

horizontal = Scale(root, from_=200, to=700, orient=HORIZONTAL)
horizontal.pack()


def slide():
    my_label = Label(root, text=horizontal.get())
    my_label.pack()
    root.geometry(str(horizontal.get()) + "x" + str(vertical.get()))


my_button = Button(root, text="Click me!", command=slide)
my_button.pack()

root.mainloop()
