# Python code to count number of unique matching characters in a pair of strings

def count(str1 ,str2) :
	set_string1 = set(str1)
	set_string2 = set(str2)
	matched_characters = set_string1 & set_string2
	print("No. of matching characters are : " + str(len(matched_characters)) )

str1 = 'aabcddekll12@' 
str2 = 'bb2211@55k'	 
count( str1 , str2 )
	
