#WAP to Copy NumPy array into another array
import numpy as np
  
ary = np.array([13, 99, 100, 34, 65, 11, 
                66, 81, 632, 44])
  
print("Original array: ")
  
print(ary)
  
copy = np.empty_like(ary)
  
copy[:] = ary
  
print("\nCopy of the given array: ")
  
print(copy)
