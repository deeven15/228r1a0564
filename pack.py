from tkinter import *

a=Tk()

a.title("welcome")

a.geometry("500x500")

b=Button(a,text="login")
b.pack(side=LEFT)
b2=Button(a,text="submit")
b2.pack(side=RIGHT)
a.mainloop()