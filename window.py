from tkinter import *
from tkinter import messagebox
a=Tk()
a.geometry("500x500")
a.title("hello")

def fun():
    messagebox.showinfo("hello","successfully submitted")
b=Button(a,text="login",command=fun)
b.pack(side=TOP)
a.mainloop()
