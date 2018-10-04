from tkinter import *
from tkinter import messagebox
top = Tk()
top.geometry("400x500")
def actioner():
	msg = messagebox.showinfo("Success","The number has been entered ")
ent = Entry(top,font="50px")
ent.place(x = 100,y = 50)
b1 = Button(top,text = "1",command=actioner, width=5,
	height = 2)
b1.place(x = 100,y = 100)
b2 = Button(top,text = "2",command =  actioner, width = 5,
	height = 2)
b2.place(x = 150,y = 100)
b3 = Button(top,text = "3",command =  actioner, width = 5,
	height = 2)
b3.place(x = 200,y = 100)
b13 = Button(top,text = "+",command =  actioner, width = 5,
	height = 2)
b13.place(x = 250,y = 100)
b4 = Button(top,text = "4",command =  actioner, width = 5,
	height = 2)
b4.place(x = 100,y = 150)
b5 = Button(top,text = "5",command =  actioner, width = 5,
	height = 2)
b5.place(x = 150,y = 150)
b6 = Button(top,text = "6",command =  actioner, width = 5,
	height = 2)
b6.place(x = 200,y = 150)
b14 = Button(top,text = "-",command =  actioner, width = 5,
	height = 2)
b14.place(x = 250,y = 150)
b7 = Button(top,text = "7",command =  actioner, width = 5,
	height = 2)
b7.place(x = 100,y = 200)
b8 = Button(top,text = "8",command =  actioner, width = 5,
	height = 2)
b8.place(x = 150,y = 200)
b9 = Button(top,text = "9",command =  actioner, width = 5,
	height = 2)
b9.place(x = 200,y = 200)
b15 = Button(top,text = "*",command =  actioner, width = 5,
	height = 2)
b15.place(x = 250,y = 200)
b10 = Button(top,text = "/",command =  actioner, width = 5,
	height = 2)
b10.place(x = 100,y = 250)
b11 = Button(top,text = "0",command =  actioner, width = 5,
	height = 2)
b11.place(x = 150,y = 250)
b12 = Button(top,text = "DEL",command =  actioner, width = 5,
	height = 2)
b12.place(x = 200,y = 250)
b16 = Button(top,text = "=",command =  actioner, width = 5,
	height = 2)
b16.place(x = 250,y = 250)
top.mainloop()