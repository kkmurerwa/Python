import Tkinter
import tkMessageBox
top=Tkinter.Tk()

def helloCallBack():
	tkMessageBox.showinfo("Hello Python", "Hello world\n")

B = Tkinter.Button(top, text="Hello", command=helloCallBack)

B.pack()
top.mainloop()