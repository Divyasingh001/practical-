#Multiply Adjacent elements
test_tup = (1, 5, 7, 8, 10)
  

print("The original tuple : " + str(test_tup))
  

res = tuple(i * j for i, j in zip(test_tup, test_tup[1:]))
  

print("Resultant tuple after multiplication : " + str(res))
