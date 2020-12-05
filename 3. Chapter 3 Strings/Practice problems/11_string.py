'''Write a Python program to remove the characters which have odd index values of a given string.'''
# def odd_string(str1):
#     return str1[0::2]
#
# print(odd_string('abc'))

def odd_string(str):
    result = ""
    for i in range(len(str)):
        if i%2 == 0:
            result = result+str[i]
    return result
print(odd_string('abcdef'))
print(odd_string('python'))