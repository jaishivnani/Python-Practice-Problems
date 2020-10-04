'''Write a Python program to get a string from a given string 
where all occurrences of its first char have been changed to '$', except the first char itself.'''


def string(str):
    char = str[0].lower()
    str = str.replace(char,'$')
    return char + str[1:]
    # return str[0].lower() + str[1:].replace(str[0].lower(),'$') # - In One Line


print(string("Character"))
print(string("Easy and affordable"))
    

   