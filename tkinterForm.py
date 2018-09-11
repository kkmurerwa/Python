from tkinter import *
from tkinter import messagebox

class FormDisplayer:
    def __init__(self, master):#This is the class constructor
        self.master = master
        master.title("Input form")#Sets the master title as form
        self.label = Label(text= "This is an input form".capitalize())
        self.label.pack()
        self.label = Label(text="------------------------------------------------------------------------")
        self.label.pack()
        self.label1 = Label(text = "First Name   ")
        self.label1.place(x = 64, y= 52.5)
        self.firstname = Entry()
        self.firstname.place(x = 170, y = 50, height = 25, width = 200)#Defines the length and size of the text item
        self.lnameLabel = Label(text = "Last Name  ")
        self.lnameLabel.place(x = 64, y = 92.5)
        self.lastname = Entry()
        self.lastname.place(x = 170, y = 92, height = 25, width = 200)
        self.ageLabel = Label(text="Age \t  ")
        self.ageLabel.place(x=64, y=132.5)
        self.age = Entry()
        self.age.place(x=170, y=132, height=25, width=200)
        self.emailLabel = Label(text="Email \t  ")
        self.emailLabel.place(x=64, y=172.5)
        self.email = Entry()
        self.email.place(x=170, y=172, height=25, width=200)

        self.submit = Button(text="Submit", command = self.messenger)
        self.submit.place(x = 125, y = 212)
        close = Button(text="Exit", command = self.exiter)
        close.place(x=200, y=212)
    def exiter(self):
        sys.exit()

    def messenger(self):
        message = messagebox.showinfo("Message Box", f"Hello {self.firstname.get()} {self.lastname.get()}\n"
                                                     f"You are {self.age.get()} years old\nYour email is {self.email.get()}")
root = Tk()
root.geometry("400x250+500+250")
#The first two coordinates dictate the size and the last two the positioning on the screen
gui_form = FormDisplayer(root)#Create an instance of FormDisplayer
root.mainloop()


