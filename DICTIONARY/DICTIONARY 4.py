#WAP to check number of keys have same value.
empdict = {'Racx': 12000, 'Max':80000,'Stack':80000,'John':80000,}
valuetofind = 80000

count = sum(val == valuetofind for val in empdict.values())  
  
print("number of keys have same value : " ,count) 
