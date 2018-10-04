from tkinter import *
from tkinter import messagebox
top = Tk()
top.geometry("400x400")
def exit():
	box = messagebox.showinfo("I am exiting")
Button1 = Button(top,text = "hello", command = exit)
Button1.place(x=200,y=200)
top.mainloop()
