#Write a function in python to read the content from a text file "poem.txt"
#line by line and display the same on screen.
def count_words():
    file = open("notes.txt","r")
    count = 0
    data = file.read()
    words = data.split()
    for word in words:
        count += 1
    print("Total words are",count)
    file.close()

count_words()

