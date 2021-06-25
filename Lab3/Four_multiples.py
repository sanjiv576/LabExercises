"""
Write a function that returns the sum of multiples of 3 and 5 between 0
and limit (parameter). For example, if limit is 20, it should return the sum of 3, 5, 6,
9, 10, 12, 15, 18, 20
"""
def myFunc(limit):
    limitation = limit
    add = 0
    add1 = 0
    for loop in range(1,limit+1):
        forThree = loop * 3
        if forThree <= limitation:
            add += forThree
        forFive = loop * 5
        if forFive <= limitation:
            add1 += forFive
    addition = add + add1
    return addition

    return add
print(myFunc(20))
