from tkinter import *;
from tkinter import  messagebox
import pymysql
import pymysql.cursors



class LoginPage:#Creates a class window to hold all items
    def __init__(self, master):
        self.master = master
        master.title("Login Page")

    def createLabels(self):
        userlabel = Label(text = "Username")
        userlabel.place(x=80,y=50)
        passlabel = Label(text = "Password")
        passlabel.place(x=80, y=100)

    def entryBoxes(self):
        self.username = Entry(root)
        self.username.place(x=150,y=50)
        self.password = Entry(root, show = "*")
        self.password.place(x=150,y=100)

    def createSubmit(self):
        submit = Button(text = "Submit",height=2, width = 10, command = self.authentication)
        submit.place(x=110,y=130)

    def authentication(self):
        user = self.username.get()#Gets username from the username entry box
        pwd = self.password.get()#Gets password from the password entry box

        conn = pymysql.connect(host='localhost', user='root', password='toor', db='pythonlogin', charset='utf8mb4',
                               cursorclass=pymysql.cursors.DictCursor)
        a = conn.cursor()
        usernamecheck = a.execute("SELECT * FROM login where username = '" + user + "'")
        passwrddb = a.fetchall()

        for record in passwrddb:
            if record["username"] == user:
                if record["password"] == pwd:
                    print("Login successful")
                else:
                    print("Password Incorrect")
            else:
                print("Username not found")
root = Tk()
root.geometry("450x300")
my_gui = LoginPage(root)
my_gui.createLabels()
my_gui.entryBoxes()
my_gui.createSubmit()
root.mainloop()
