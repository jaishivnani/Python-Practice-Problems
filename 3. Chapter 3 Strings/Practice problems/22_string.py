'''Write a Python function to convert a given string to all uppercase
if it contains at least 2 uppercase characters in the first 4 characters.'''

def to_uppercase(str):
    num_upper=0
    for letter in str[0:4]:
        if letter.upper()==letter:
            num_upper+=1
    if num_upper>=2:
        return str.upper()
    return str

print(to_uppercase('GeeksforGeeks'))
print(to_uppercase('GEeksforGeeks'))
print(to_uppercase('GEEksforGeeks'))




