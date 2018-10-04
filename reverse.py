c=0
a=input("Enter the number to reverse \n")
while a>=1:
	b=a % 10
	a=a / 10
	c=c*10+b
print("The reversed number is :",c)