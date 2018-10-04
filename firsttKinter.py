from tkinter import *#imports the tkinter library
from tkinter import messagebox
from functools import partial

#This is a OOP implementation of a python window using classes and methods
class MyFirstGUI:#Creates class
    def __init__(self, master):#creates class constructor
        self.master = master
        master.title("First GUI")
        self.label = Label(master,text = "This is our first label")
        self.label.pack()
        self.message_button  = Button(master, text = "Press Me", command = self.message)
        self.message_button.pack()
        self.close_button = Button(master,text="Close",command=self.greet)
        self.close_button.pack()
    def button_creator(self,stik):
        butt = Button(text = stik)
        butt.pack()
    def create_labels(self):
        lab1 = Label(text = "I am another Label")
        lab2 = Label(text = "I am a third Label")
        lab1.pack()
        lab2.pack()
    def message(self):
        message = messagebox.showinfo("Success","I am a message embeddded in a button")
    def greet(self):
        import sys;sys.exit(0)
root = Tk()
root.geometry("400x250")
my_gui = MyFirstGUI(root)#calls instance of class MyFirstGUI
my_gui.create_labels()
my_gui.button_creator("I do Nothing")
root.mainloop()