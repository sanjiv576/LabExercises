"""Write a function called showNumbers that takes a parameter called limit. It
should print all the numbers between 0 and limit with a label to identify the even and
odd numbers. For example, if the limit is 3, it should print:
0 EVEN
1 ODD
2 EVEN"""


def showNumbers(limit):
    for i in range(limit+1):
        if i % 2 == 0:
            print(f"{i} EVEN")
        else:
            print(f"{i} ODD")


limit = int(input("Enter the number : "))
showNumbers(limit)
