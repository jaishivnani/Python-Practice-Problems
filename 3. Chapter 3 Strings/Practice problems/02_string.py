'''Write a Python program to count the number of characters (character frequency) in a string.'''
'''It is the simplest way to count the character frequency in a Python string. You can take a dictionary,
use its keys to keep the char, and the corresponding values for the no. of occurrences. 
It just requires to keep incrementing each value field by 1.'''

'''Solution 1'''

String = "Python is very simple and user friendly language."
frequencies = {}
for char in String:
    frequencies[char] = frequencies.get(char,0)+1

print("Per Char frequency in String is '{}' is :\n{}".format(String,str(frequencies)))


'''Solution 2'''
# from collections import Counter
#
# String = "Python is very simple and user friendly language."
#
# frequencies = Counter(String)
#
# print("Per Char Frequency in String is '{}' is :\n{}".format(String,str(frequencies)))

'''Solution 3'''
# String = "Python is very simple and user friendly language."
#
# frequencies={}
#
# for char in String:
#     if char in frequencies:
#         frequencies[char]+=1
#     else:
#         frequencies[char]=1
#
# print("Per Char Frequency in String is '{}' is :\n{}".format(String,str(frequencies)))

# '''Solution 4'''
# String = "Python is very simple and user friendly language."
#
# frequencies={}
# def string_length(str):
#     for char in str:
#         if char in frequencies:
#             frequencies[char]+=1
#         else:
#             frequencies[char]=1
#     return frequencies
#
# print("Per Char Frequency in String is '{}' is :\n{}".format(string_length("Jjai")))
# Show Output
# print("Per Char Frequency in String is '{}' is :\n{}".format(String,str(frequencies)))
# print(str(frequencies))   

# Time Complexity = 5n + 4 = O(n)



