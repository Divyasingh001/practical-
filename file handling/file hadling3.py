# Write a function in Python to count uppercase character in a text file.
def count_letter():
    file = open("article.txt","r")
    data = file.read()
    count = 0
    for letter in data:
        if letter.isupper():
            count+=1
    print(count)
    file.close()

count_letter()
