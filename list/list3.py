# Python program to find smallest number in a list

l=[ int(l) for l in input("List:").split(",")]
print("The list is ",l)
min1 = l[0]
for i in range(len(l)):
	if l[i] < min1:
		min1 = l[i] #It will change
print("The smallest element in the list is ",min1)
