'''Dictionary Membership Test
We can test if a key is in a dictionary or not using the keyword in.
Notice that the membership test is only for the keys and not for the values.'''

# Membership Test for Dictionary Keys
squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}

# Output: True
# For Keys
print(1 in squares)
print(1 in squares.keys())

# Output: True
# For Keys
print(2 not in squares)

# For Values
# Output: False
print(49 in squares.values())

sampleDict = {'a': 100, 'b': 200, 'c': 300}
print(200 in sampleDict.values())

