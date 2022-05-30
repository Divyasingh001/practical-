# Sum of digits of elements in List

test_list = [12, 67, 98, 34]
print("The original list is : " + str(test_list))
res = []
for ele in test_list:
	sum = 0
	for digit in str(ele):
		sum += int(digit)
	res.append(sum)
print ("List Integer Summation : " + str(res))
