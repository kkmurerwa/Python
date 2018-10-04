from tkinter import *
from tkinter import messagebox;
top = Tk()
top.geometry("400x500")#sets dimensions for the tkinter box
def hellocallback():
	msg = messagebox.showinfo("Hello python","hello world")
B = Button(top,text = "hello",command = hellocallback,width = 5,
height = 5)
entr =  Entry(top,font="100px");
entr.place(x = 100,y = 50)
B.place(x=350,y=350)#sets placement of the button
top.mainloop()