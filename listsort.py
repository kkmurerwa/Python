soap = [95,50,67]
deo = [325,250,400]
tissue = [25,35,30]
soapsorted = soap.sort(key=int)
deosorted = deo.sort(key=int)
tissuesorted = tissue.sort(key=int)
total = soapsorted[0]+deosorted[0]+tissuesorted[0]
print (total)