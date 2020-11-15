'''Exercise Question 4:
Arrange string characters such that lowercase letters should come first
Sample Input
str1 = PyNaTive
Sample Output
yaivePNT
'''

str1 = "PyNaTive"
def lowerfirst(str1):
    lower = []
    upper = []
    for char in str1:
        if char.islower():
            lower.append(char)
        else:
            upper.append(char)
    sorted_string=''.join(lower+upper)
    print(sorted_string)

lowerfirst(str1)









