from tkinter import *
from PIL import ImageTk, Image

win = Tk()
win.title("Learn to Code")
win.iconbitmap("Cabeza.ico")

my_img1 = ImageTk.PhotoImage(Image.open("images/Iphone_1.png"))
my_img2 = ImageTk.PhotoImage(Image.open("images/Iphone_2.png"))
my_img3 = ImageTk.PhotoImage(Image.open("images/Iphone_3.png"))
my_img4 = ImageTk.PhotoImage(Image.open("images/Iphone_4.png"))
my_img5 = ImageTk.PhotoImage(Image.open("images/Iphone_5.png"))
my_img6 = ImageTk.PhotoImage(Image.open("images/Iphone_6.png"))

image_list = [my_img1, my_img2, my_img3, my_img4, my_img5, my_img6]

status = Label(win, text="Image 1 of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)

my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)


def forward(img_num):
    global my_label
    global forward_button
    global back_button

    my_label.grid_forget()
    my_label = Label(image=image_list[img_num - 1])
    forward_button = Button(win, text=">>", command=lambda: forward(img_num + 1))
    back_button = Button(win, text="<<", command=lambda: back(img_num - 1))

    if img_num == 6:
        forward_button = Button(win, text=">>", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    back_button.grid(row=1, column=0)
    forward_button.grid(row=1, column=2)
    
    status = Label(win, text="Image " + str(img_num) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)


def back(img_num):
    global my_label
    global forward_button
    global back_button

    my_label.grid_forget()
    my_label = Label(image=image_list[img_num - 1])
    forward_button = Button(win, text=">>", command=lambda: forward(img_num + 1))
    back_button = Button(win, text="<<", command=lambda: back(img_num - 1))

    if img_num == 1:
        back_button = Button(win, text="<<", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    back_button.grid(row=1, column=0)
    forward_button.grid(row=1, column=2)

    status = Label(win, text="Image " + str(img_num) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)


back_button = Button(win, text="<<", command=back, state=DISABLED)
exit_button = Button(win, text="EXIT", command=win.quit)
forward_button = Button(win, text=">>", command=lambda: forward(2))

back_button.grid(row=1, column=0)
exit_button.grid(row=1, column=1)
forward_button.grid(row=1, column=2, pady=10)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)

win.mainloop()
