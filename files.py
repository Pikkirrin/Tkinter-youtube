from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title("Images viewer")
root.iconbitmap("Head.ico")


def open():
    global my_image
    root.filename = filedialog.askopenfilename(
        initialdir="/Users/VictorHGH/Documents/Programación/Tkinter-youtube/images",
        title="Select a file",
        filetypes=(("png files", "*.png"), ("all files", "*.*"))
    )

    my_image = ImageTk.PhotoImage(Image.open(root.filename))

    my_label = Label(root, image=my_image)
    my_label.grid(row=0, column=0)


my_button = Button(root, text="open file", command=open)
my_button.grid(row=1, column=0)

mainloop()
