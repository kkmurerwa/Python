eng=input("enter the marks gotten in english\n")
math=input("enter the marks gotten in math\n")
kisw=input("enter the marks gotten in kiswahili\n")
total=eng+math+kisw
average=total/3
if average>100 or average<0 :
	print"The marks entered exceed the range of 0 to 100"
elif average>=70 :
	print"Grade:A"
elif average>=60 :
	print"Grade:B"
elif average>=50 :
	print"Grade:C"
elif average>=40 :
	print"Grade:D"
else :
	print"Grade:F"