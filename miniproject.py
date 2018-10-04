def grading(average):
	if (marks>=70) and (marks<=100):
		grade='A'
	elif(marks>=60):
		grade='B'
	elif(marks>=50):
		grade='C'
	elif(marks>=40):
		grade='D'
	else:
		grade='F'
	print "The student got grade : ",grade
	return grade;

def line():
	print "==========================================================\n"
	
def clusterone():
	maths=input("Enter the marks attained in mathematics\n")
	eng=input("Enter the marks attained in English\n")
	phy=input("Enter the marks attained in Physics\n")
	average=maths+eng+phy
	if (average>=50):
		line();
		print "CONGRATULATIONS! You qualify to join Maseno University\n"
		if (average>=60):
			print "You qualify to study Computer Science\n"
		else:
			print "You do not qualify to study Computer Science\n"
	else:
		print "Sorry. You do not qualify to join Maseno University\n"
	line();

def clustertwo():
	maths=input("Enter the marks attained in Mathematics\n")
	eng=input("Enter the marks attained in Physics\n")
	chem=input("Enter the marks attained in Chemistry\n")
	average=maths+eng+chem
	grading(average);
	if (average>=50):
		line();
		print "CONGRATULATIONS! You qualify to join Maseno University\n"
		print "You qualify to study Computer Science\n"
	else:
		print "Sorry. You do not qualify to join Maseno University\n"
	line();
	
select=input("Enter one or two\n")
if (select==1):
	clusterone();
elif (select==2):
	clustertwo();
else:
	print "The number entered is out of range\n"

