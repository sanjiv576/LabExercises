# Accept string from the user and display only those characters which are present at an even index

def characters(string):
    counter = 0
    for i in string:
        counter += 1
        if counter % 2 == 0:
            print(i)


string = input("Input a string : ")
characters(string)


