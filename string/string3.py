#Remove all duplicate characters from a given string in Python
def removeDuplicate(str):
	s=set(str)
	s="".join(s)
	t=""
	for i in str:
		if(i in t):
			pass
		else:
			t=t+i
	print("Final string:",t)
	
str="geeksforgeeks"
removeDuplicate(str)
