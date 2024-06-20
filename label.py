from tkinter import *
from PIL import ImageTk
import mysql.connector


def saveData():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="  ",
        database="customerdata"
    )


window = Tk()
background = ImageTk.PhotoImage(file='azad.jpeg')
blabel = Label(window, image=background)
blabel.grid()
frame = Frame(window)
frame.place(x=600, y=100)

usernameLabel = Label(frame, text="username", font=('Arial', 15, 'bold'), bg='white', fg='firebrick')
usernameLabel.grid(row=0, column=0, padx=10, pady=5)  # Add padx and pady to create space

usernameEntry = Entry(frame, width=30)
usernameEntry.grid(row=0, column=1)

emailLabel = Label(frame, text="email", font=('Arial', 15, 'bold'), bg='white', fg='firebrick')
emailLabel.grid(row=1, column=0)
emailEntry = Entry(frame, width=30)
emailEntry.grid(row=1, column=1)

passwordLabel = Label(frame, text="password", font=('Arial', 15, 'bold'), bg='white', fg='firebrick')
passwordLabel.grid(row=2, column=0, padx=10, pady=5)
passwordEntry = Entry(frame, width=30)
passwordEntry.grid(row=2, column=1)

window.mainloop()