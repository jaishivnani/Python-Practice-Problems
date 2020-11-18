#sets in Python

'''Creating an empty set is a bit tricky.

Empty curly braces {} will make an empty dictionary in Python.
To make a set without any elements, we use the set() function without any argument.'''

# Distinguish set and dictionary while creating empty set

# initialize a with {}
a = {}

# check data type of a
print(type(a))

# initialize a with set()
a = set()

# check data type of a
print(type(a))
