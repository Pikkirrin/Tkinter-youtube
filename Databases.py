from tkinter import *
import sqlite3

root = Tk()
root.title("check Boxes")
root.iconbitmap("Head.ico")
root.geometry("400x400")

# Databases

# Create a database or connect to one
conn = sqlite3.connect('address_book.db')

# Create a cursor
c = conn.cursor()

# Create a table
'''
c.execute("""CREATE TABLE addresses (
        first_name text,
        last_name text,
        address text,
        city text,
        state text,
        zipcode integer
        )""")
'''

# Commit Changes
conn.commit()

# Close Connection
conn.close()

root.mainloop()
