#Python program to calculate the sum and average of n integer numbers.
#Input 0 to finish.

print("Input some integers to calculate their sum and average.")
count = 0
sum = 0.0
number = 1
while number != 0:
	number = int(input(""))
	sum = sum + number
	count += 1
if count == 0:
	print("Input some numbers")
else:
	print("Average and Sum of the above numbers are: ", sum / (count-1), sum)
