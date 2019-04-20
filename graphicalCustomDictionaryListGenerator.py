from tkinter import *
from tkinter import messagebox
import textwrap

class FormDisplayer:
    def __init__(self, master):#This is the class constructor
        self.master = master
        master.title("Input form")#Sets the master title as form
        self.label = Label(text= "Enter Info Below".capitalize())
        self.label.pack()
        self.label = Label(text="------------------------------------------------------------------------")
        self.label.pack()
        # First name
        self.label1 = Label(text = "First Name   ")
        self.label1.place(x = 50, y= 52.5)
        self.firstname = Entry()
        self.firstname.place(x = 170, y = 50, height = 25, width = 200)#Defines the length and size of the text item
        
        # Middle name
        self.mnameLabel = Label(text = "Middle Name  ")
        self.mnameLabel.place(x = 50, y = 92.5)
        self.middlename = Entry()
        self.middlename.place(x = 170, y = 90, height = 25, width = 200)

        #Last name
        self.lnameLabel = Label(text = "Last Name  ")
        self.lnameLabel.place(x = 50, y = 132.5)
        self.lastname = Entry()
        self.lastname.place(x = 170, y = 130, height = 25, width = 200)

        #ID Number
        self.idLabel = Label(text = "ID No.  ")
        self.idLabel.place(x = 50, y = 172.5)
        self.id = Entry()
        self.id.place(x = 170, y = 170, height = 25, width = 200)

        #Date of birth
        self.dobLabel = Label(text = "Date of Birth(only)  ")
        self.dobLabel.place(x = 50, y = 212.5)
        self.dob = Entry()
        self.dob.place(x = 170, y = 210, height = 25, width = 200)

        #Year of birth
        self.yobLabel = Label(text="YOB \t  ")
        self.yobLabel.place(x=50, y=292.5)
        self.yob = Entry()
        self.yob.place(x=170, y=250, height=25, width=200)

        #Email
        self.emailLabel = Label(text="Email \t  ")
        self.emailLabel.place(x=50, y=332.5)
        self.email = Entry()
        self.email.place(x=170, y=290, height=25, width=200)

        #Submit button
        self.submit = Button(text="Submit", command = self.messenger)
        self.submit.place(x = 125, y = 372)

        #Exit button
        close = Button(text="Exit", command = self.exiter)
        close.place(x=200, y=372)

    def exiter(self):
        #This method exits the program
        sys.exit()

    def messenger(self):
        #This method picks information from the form and generates a custom dictionary list

        # Select 
        fname = self.firstname.get()
        lname = self.lastname.get()
        mname = self.middlename.get()
        idno = self.id.get()
        dobInt = int(self.dob.get())
        yobInt = int(self.yob.get())
        additionalInfo = self.firstname.get()
        fnameinitial = textwrap.shorten(fname,width=1, placeholder="")#shortens firstname to an initial
        lnameinitial = textwrap.shorten(lname,width=1, placeholder="")#shortens lastname to an initial
        mnameinitial = textwrap.shorten(mname,width=1, placeholder="")#shortens midddlename to an initial
        yob = str(yobInt)
        dob = str(dobInt)
        #write items to file here
        #Code below outputs the generated list with a filename that has the victims names
        file = open ("C:/Users/Kenneth Murerwa/Documents/GeneratedCustomPasswordList/"+fname+lname+".txt","w")
        file.write(fname+" "+lname+" "+"passwordlist"+"\n")
        file.write(idno+"\n")
        file.write(fname+dob+"\n")
        file.write(fname+lnameinitial+dob+"\n")
        file.write(fname+lname+dob+"\n")
        file.write(lname+dob+"\n")
        file.write(lname+fnameinitial+dob+"\n")
        file.write(lname+fname+dob+"\n")
        file.write(mname+dob+"\n")
        file.write(mname+fnameinitial+dob+"\n")
        file.write(mname+fname+dob+"\n")
        file.write(fname+str(yob)+"\n")
        file.write(lname+str(yob)+"\n")
        file.write(fname+lname+str(yob)+"\n")
        file.write(lname+fname+str(yob)+"\n")
        file.write(fname+lnameinitial+str(yob)+"\n")
        file.write(lname+fnameinitial+str(yob)+"\n")
        
        # 
        if yobInt >=2000 and yobInt<2010:
            yobInt-=2000
            yob = str(yobInt)
            dob = str(dobInt)
            file.write(fname + "0" + str(yob)+"\n")
            file.write(lname + "0" + str(yob)+"\n")
            file.write(fname + "0" + lname + str(yob) + "\n")
            file.write(lname + "0" + fname + str(yob) + "\n")
            file.write(fname + "0" + lnameinitial + str(yob) + "\n")
            file.write(lname + "0" + fnameinitial + str(yob) + "\n")
            file.write(fname+str(yob)+"\n")
            file.write(lname + str(yob)+"\n")
            file.write(fname + lname + str(yob) + "\n")
            file.write(lname + fname + str(yob) + "\n")
            file.write(fname + lnameinitial + str(yob) + "\n")
            file.write(lname + fnameinitial + str(yob) + "\n")
        elif yobInt>=2010:
            yobInt-=2000
            yob = str(yobInt)
            dob = str(dobInt)
            file.write(fname+str(yob)+"\n")
            file.write(lname + str(yob)+"\n")
            file.write(fname + lname + str(yob) + "\n")
            file.write(lname + fname + str(yob) + "\n")
            file.write(fname + lnameinitial + str(yob) + "\n")
            file.write(lname + fnameinitial + str(yob) + "\n")
        else:
            yobInt-=1900
            yob = str(yobInt)
            dob = str(dobInt)
            file.write(fname+str(yob)+"\n")
            file.write(lname + str(yob)+"\n")
            file.write(fname + lname + str(yob) + "\n")
            file.write(lname + fname + str(yob) + "\n")
            file.write(fname + lnameinitial + str(yob) + "\n")
            file.write(lname + fnameinitial + str(yob) + "\n")

        file.close()
        exit()
root = Tk()
root.geometry("400x450+500+250")
#The first two coordinates dictate the size and the last two the positioning on the screen
gui_form = FormDisplayer(root)#Create an instance of FormDisplayer
root.mainloop()


