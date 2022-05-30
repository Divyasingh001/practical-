#Custom sorting in list of tuples
test_list = [(7, 8), (5, 6), (7, 5), (10, 4), (10, 1)]

print("The original list is : " + str(test_list))
res = sorted(test_list, key = lambda sub: (-sub[0], sub[1]))

print("The tuple after custom sorting is : " + str(res))
