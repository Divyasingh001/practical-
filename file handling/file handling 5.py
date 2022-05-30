#Create a text file “intro.txt” in python and ask the user
#to write a single line of text by user input.
def program1():
    f = open("intro.txt","w")
    text=input("Enter the text:")
    f.write(text)
    f.close()
program1()
