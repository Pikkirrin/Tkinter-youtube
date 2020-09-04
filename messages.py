from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Messages")
root.iconbitmap("Head.ico")
root.geometry("300x50")


# type of message box = showinfo, showwarning, showerror, askquestion, askokcancel, askyesno
# askyesno return = 1/0
# askokcancel return = 1/0
# askquestion return = yes/no
# showerror return = ok
# showwarning return = ok
# showinfo return = ok
def popup():
    response = messagebox.showinfo("This is my popup", "Hello world")
    Label(root, text=response).grid(row=1, column=0)
    if response == "yes":
        Label(root, text="You click yes").pack()
    else:
        Label(root, text="You click no").pack()


Button(root, text="Popup", command=popup, fg="red").pack()

root.mainloop()
