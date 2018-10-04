from tkinter import *

#The code below has the GUI layout of a music player based on TKinter

class FormDisplayer:
    def __init__(self, master):
        self.master = master
        canvas = Canvas(root, width=600, height=150)
        color = 'red'
        self.num = 500
        canvas.create_rectangle(500, 50, 100, 150, fill=color)#Coordinates are length, x-axis, y-axis, height
        canvas.pack()
        self.w = Scale(master, from_=0, to=self.num, length = 400, orient = HORIZONTAL)

        self.w.pack()
        self.def_val = 0
        self.messenger()
    def messenger(self):
        #print(self.w.get())#Gets value of slider and changes the color
        if (self.w.get()<self.num):
            self.w.set(self.def_val+1)#sets value of slider
        else:
            self.w.set(0)
        root.after(1000, self.messenger())


root = Tk()
root.title("Ken Music PLayer")
root.geometry("600x400+500+250")
#The first two coordinates dictate the size and the last two the positioning on the screen
gui_form = FormDisplayer(root)#Create an instance of FormDisplayer
root.mainloop()