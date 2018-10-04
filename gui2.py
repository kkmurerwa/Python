import tkinter
from tkinter import *

ken = Tk("Window")
ken.geometry("400x400")
var1 = IntVar()
var2 = IntVar()
check1 = Checkbutton(ken,text="male",variable=var1,height=5,width=10)
check2 = Checkbutton(ken,text="female",variable=var2,height=5,width=10)
label1 = Label(ken,text="First Name")
label1.pack(side=LEFT)
txtbox=Entry(ken,bd=2,justify=CENTER)
txtbox.pack(side=RIGHT)
check1.pack()
check2.pack()
ken.mainloop()