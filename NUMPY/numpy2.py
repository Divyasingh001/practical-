# WAP to create an empty and a full NumPy array?
import numpy as np
  
empa = np.empty((3, 4), dtype=int)
print("Empty Array")
print(empa)
  
flla = np.full([3, 3], 55, dtype=int)
print("\n Full Array")
print(flla)
