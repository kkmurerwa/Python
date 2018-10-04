from tkinter import *

root = Tk()
root.geometry("400x500")#sets the dimensions of the main window
w = Label(root,text = "Hello world")
b = Button(root,text="Quit",width = 15,height = 5,action = root.quit())#Creates a button that exits the window
w.place(x = 10,y = 10)
b.place(x = "20px",y = "30px")
root.mainloop()