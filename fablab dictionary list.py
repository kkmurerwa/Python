import textwrap

#Enter the inputs here


#write items to file here
#Code below outputs the generated list with a filename that has the victims names
file = open ("C:/Users/Kenneth Murerwa/Documents/GeneratedCustomPasswordList/FablabWinam"+".txt", "w")
stringKnownPart = "TekTech"
for i in range(10, 99):
    file.write(stringKnownPart+str(i)+"\n")


file.close()
exit()
