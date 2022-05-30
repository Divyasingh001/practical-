'''
Printing a Pattern of Unique Digits Using a Pyramid
1 

1 2 1 

1 2 3 2 1 

1 2 3 4 3 2 1
'''
n = int(input())

for k in range(1, n + 1):

    for m in range(1, k-1):

        print(m, end=" ")

    for m in range(k-1, 0, -1):

        print(m, end=" ")

    print()
