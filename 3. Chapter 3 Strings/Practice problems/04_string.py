'''Write a Python program to get a string from a given string 
where all occurrences of its first char have been changed to '$', except the first char itself.'''


def string(str):
    char = str[0].lower()           #Storing 1st character in lower
    str = str.replace(char,'$')     #Doing str = str.replace(char,'$') for replacing 1st character and its occurences to $.
    return char + str[1:]           #Returning char stored in line 6 + str[1:](String starting from position 1 to ...)
    # return str[0].lower() + str[1:].replace(str[0].lower(),'$') # - In One Line


print(string("Character"))
print(string("Easy and affordable"))
    

   