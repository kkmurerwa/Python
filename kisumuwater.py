def clityp():
	print("Enter the number representing the type of user\n")
	print("1.Metered\n2.Unmetered\n")
	client=int(input())
	return client

def units():
	unit=int(input("Enter the number of units used\n"))
	return unit
def payinfo():
	payme=input("Select payment method\n1.VISA(5% discount)\n2.Cash\n")
	return payme

def outp(bill):
	print("Your total bill is: ",bill)

def met():
	unit = units()
	if (unit<150):
		bill = unit*33
		if (int(payinfo())==1):
			discount=bill*5/100
		else:
			discount=0;
	outp(bill-discount)

def unmet():
	pass

def main():
	if (clityp()==1):
		met()
	elif (clityp()==2):
		unmet()
	else:
		print("The number entered is not valid")
		
main();
	