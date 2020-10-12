'''Write a Python program to add 'ing' at the end of a given string (length should be at least 3). 
If the given string already ends with 'ing' then add 'ly' instead. 
If the string length of the given string is less than 3, leave it unchanged'''

def string(str):
    if len(str) < 3:
        return str
    elif len(str)>=3 and not str.endswith("ing"):
        return str + 'ing'  
    else:
        str.endswith("ing")
        return str + 'ly'     

print(string("ab"))
print(string("abc")) 
print(string("string")) 