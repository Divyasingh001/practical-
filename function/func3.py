#Python program to check whether a number is Prime or not
def isprime(num):
    if num > 1:
        for i in range(2, int(num/2)+1):
            if (num % i) == 0:
                print(num, "is not a prime number")
                break
        else:
            print(num, "is a prime number")
  
    else:
        print(num, "is not a prime number")
num=int(input())
isprime(num)
