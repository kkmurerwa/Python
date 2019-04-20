import textwrap
import itertools
# Enter the inputs here
array1 = []
array2 = []
array1.append(input("Enter first name\n"))
array1.append(input("Enter middle name\n"))
array1.append(input("Enter last name\n"))
# idno = (input("Enter id number\n"))
# array2.append(input("Enter date of birth. Date only\n"))
# array2.append(input("Enter year of birth\n"))
# additionalInfo = input("Enter number of additional details you would like to add")


perm = itertools.permutations(array1, 2)
for i in perm:
    print(i)

# Add the for statements to simplify the generation of the dictionary list
# # print(idno)
# for i in range(0, len(array1)):
#     for j in range(0, len(array1)):
#         if i!=j:
#             if i > 0:
#                 # Do some stuff
#                 print(array1[i] + array1[j])
#             else:
#                 print(array1[j])
#                 # Do other stuff
#         elif i==0:
#             if j > 0:
#                 # Do some stuff
#                 print(array1[i] + array1[j])
#             else:
#                 print(array1[j])
#                 # Do other stuff
#         else:
#             continue
        


#Add input entry for middle name and month of birth
# Add an option for the user to add any additional information such as
# favorite pet, home town or
#Modify the inputs to any format you want here
# ==========================================================================
# Deduce the initials of the victim
# fnameinitial = textwrap.shorten(fname,width=1, placeholder="")#shortens firstname to an initial
# lnameinitial = textwrap.shorten(lname,width=1, placeholder="")#shortens lastname to an initial
# mnameinitial = textwrap.shorten(mname,width=1, placeholder="")#shortens midddlename to an initial


# print(array1)
#write items to file here
#Code below outputs the generated list with a filename that has the victims names
# file = open ("C:/Users/Kenneth Murerwa/Documents/GeneratedCustomPasswordList/"+fname+lname+".txt","w")
# file.write(fname+" "+lname+" "+"passwordlist"+"\n")
# file.write(idno+"\n")



# file.write(fname+dob+"\n")
# file.write(fname+lnameinitial+dob+"\n")
# file.write(fname+lname+dob+"\n")
# file.write(lname+dob+"\n")
# file.write(lname+fnameinitial+dob+"\n")
# file.write(lname+fname+dob+"\n")
# file.write(mname+dob+"\n")
# file.write(mname+fnameinitial+dob+"\n")
# file.write(mname+fname+dob+"\n")

# file.write(fname+str(yob)+"\n")
# file.write(lname+str(yob)+"\n")
# file.write(fname+lname+str(yob)+"\n")
# file.write(lname+fname+str(yob)+"\n")
# file.write(fname+lnameinitial+str(yob)+"\n")
# file.write(lname+fnameinitial+str(yob)+"\n")


# 
# if yob >=2000 and yob<2010:
#     yob-=2000
#     file.write(fname + "0" + str(yob)+"\n")
#     file.write(lname + "0" + str(yob)+"\n")
#     file.write(fname + "0" + lname + str(yob) + "\n")
#     file.write(lname + "0" + fname + str(yob) + "\n")
#     file.write(fname + "0" + lnameinitial + str(yob) + "\n")
#     file.write(lname + "0" + fnameinitial + str(yob) + "\n")
#     file.write(fname+str(yob)+"\n")
#     file.write(lname + str(yob)+"\n")
#     file.write(fname + lname + str(yob) + "\n")
#     file.write(lname + fname + str(yob) + "\n")
#     file.write(fname + lnameinitial + str(yob) + "\n")
#     file.write(lname + fnameinitial + str(yob) + "\n")
# elif yob>=2010:
#     yob-=2000
#     file.write(fname+str(yob)+"\n")
#     file.write(lname + str(yob)+"\n")
#     file.write(fname + lname + str(yob) + "\n")
#     file.write(lname + fname + str(yob) + "\n")
#     file.write(fname + lnameinitial + str(yob) + "\n")
#     file.write(lname + fnameinitial + str(yob) + "\n")
# else:
#     yob-=1900
#     file.write(fname+str(yob)+"\n")
#     file.write(lname + str(yob)+"\n")
#     file.write(fname + lname + str(yob) + "\n")
#     file.write(lname + fname + str(yob) + "\n")
#     file.write(fname + lnameinitial + str(yob) + "\n")
#     file.write(lname + fnameinitial + str(yob) + "\n")

# file.close()
exit()