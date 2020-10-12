'''Write a Python program to remove the characters which have odd index values of a given string.'''
def odd_string(str1):
    return str1[0::2]

print(odd_string('abcdef'))