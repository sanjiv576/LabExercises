"""Write a Python program to count the number of strings where the string length is 2
or more and the first and last character are same from a given list of strings.
Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result : 2 """

sample = ['abc', 'xyz', 'aba', '1221', 'mom', 'cat', '323']  # aba, 1221, mom, 323
result = 0
for traverse in sample:
    # length = len(traverse)
    first = traverse[:1:]  # gives first character
    last = traverse[-1:4:1]  # gives last character
    if first == last:
        result += 1
print(f"Expected result : {result}")


