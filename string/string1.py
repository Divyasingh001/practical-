# Python program to check if string is palindrome or not

def palindrome(a):
	mid = (len(a)-1)//2	
	start = 0			 
	last = len(a)-1
	flag = 0
	while(start <= mid):
		if (a[start].lower()== a[last] or a[start].upper()== a[last] ):
			start += 1
			last -= 1
		else:
			flag = 1
			break
	if flag == 0:
		print("The entered string is palindrome")
	else:
		print("The entered string is not palindrome")
		
string = 'Amaama'
palindrome(string)
