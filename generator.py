import textwrap

#Enter the inputs here

fname = input("Enter victim's first name\n")
lname = input("Enter victim's last name\n")
idno = input("Enter victim's id number\n")
dob = input("Enter victim's date of birth. Date only\n")
yob = int(input("Enter victim's year of birth\n"))

#modify the inputs to any format you want here

fnameinitial = textwrap.shorten(fname,width=1, placeholder="")#shortens firstname to an initial
lnameinitial = textwrap.shorten(lname,width=1, placeholder="")#shortens lastname to an initial
print(lnameinitial)

#write items to file here

file = open ("/root/.Hacking/generatedpassword.txt","w")
file.write(fname+" "+lname+" "+"passwordlist"+"\n")
file.write(idno+"\n")

file.write(fname+dob+"\n");
file.write(fname+lnameinitial+dob+"\n")
file.write(fname+lname+dob+"\n")
file.write(lname+dob+"\n");
file.write(lname+fnameinitial+dob+"\n")
file.write(lname+fname+dob+"\n")

file.write(fname+str(yob)+"\n")
file.write(lname+str(yob)+"\n")
file.write(fname+lname+str(yob)+"\n")
file.write(lname+fname+str(yob)+"\n")
file.write(fname+lnameinitial+str(yob)+"\n")
file.write(lname+fnameinitial+str(yob)+"\n")



if yob >=2000 and yob<2010:
    yob-=2000
    file.write(fname + "0" + str(yob)+"\n")
    file.write(lname + "0" + str(yob)+"\n")
    file.write(fname + "0" + lname + str(yob) + "\n")
    file.write(lname + "0" + fname + str(yob) + "\n")
    file.write(fname + "0" + lnameinitial + str(yob) + "\n")
    file.write(lname + "0" + fnameinitial + str(yob) + "\n")
elif yob>=2010:
    yob-=2000
    file.write(fname+str(yob)+"\n")
    file.write(lname + str(yob)+"\n")
    file.write(fname + lname + str(yob) + "\n")
    file.write(lname + fname + str(yob) + "\n")
    file.write(fname + lnameinitial + str(yob) + "\n")
    file.write(lname + fnameinitial + str(yob) + "\n")
else:
    yob-=1900
    file.write(fname+str(yob)+"\n")
    file.write(lname + str(yob)+"\n")
    file.write(fname + lname + str(yob) + "\n")
    file.write(lname + fname + str(yob) + "\n")
    file.write(fname + lnameinitial + str(yob) + "\n")
    file.write(lname + fnameinitial + str(yob) + "\n")

file.close()