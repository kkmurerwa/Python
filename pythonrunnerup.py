#This code takes input length, a number of array items separated by a space and outputs the second-highest value

def Remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list
     
if __name__ == '__main__':
	n = int(input())
	arr = map(int, input().split())#Allows input of the numbers with space in between them
	listnodup = Remove(arr)#Removes duplicates using the function Remove
	arrlist = list(listnodup);
	arrlist.sort()
	length = len(arrlist)
	print(arrlist[length-2])#Converts map to set and outputs it

