'''Write a Python program to count the length of particular characters in a string.'''

def word_length(str):

    length = [len(x) for x in str.split()]

    return length

print(word_length("Python is very simple and user friendly language."))