# Removing duplicates from tuple
test_tup = (1, 3, 5, 2, 3, 5, 1, 1, 3)
  
print("The original tuple is : " + str(test_tup))
  
res = tuple(set(test_tup))
  
print("The tuple after removing duplicates : " + str(res))
