'''Write a Python program to add 'ing' at the end of a given string (length should be at least 3). 
If the given string already ends with 'ing' then add 'ly' instead. 
If the string length of the given string is less than 3, leave it unchanged'''

def stringing(str):
    if len(str)<3:
        return str
    elif len(str)>3 and str.endswith("ing"):
        return str+"ly"
    else:
        return str+"ing"

print(stringing("ab"))
print(stringing("abc"))
print(stringing("string"))










