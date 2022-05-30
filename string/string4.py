# Python program to find all string which are greater than given length k

def string_k(k, str):
	string = []
	text = str.split(" ")
	for x in text:
		if len(x) > k:
			string.append(x)
	return string
k = 3
str ="geek for geeks"
print(string_k(k, str))
