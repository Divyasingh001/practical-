#Printing the Fibonacci series
def PrintFibonacci(length):
    first = 0
    second = 1
    print(first, second, end=" ")
    length -= 2
    while length > 0:
        print(first + second, end=" ")
        temp = second
        second = first + second
        first = temp
        length -= 1

n=int(input("Enter number of elements"))
print("Fibonacci Series - ")
PrintFibonacci(n)


