# Python Program to find palindromes in a list of strings.
  
my_list = ["geeks", "geeg", "keek", "practice", "aa"]
result = list(filter(lambda x: (x == "".join(reversed(x))), my_list)) 
print(result) 
