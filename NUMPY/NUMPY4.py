# Numpy concatenate() method

Difficulty Level : Medium
Last Updated : 03 Nov, 2019
import numpy as np
import numpy.ma as ma
  
gfg1 = np.array([1, 2, 3])
gfg2 = np.array([4, 5, 6])

gfg = ma.concatenate([gfg1, gfg2])
  
print(gfg)
