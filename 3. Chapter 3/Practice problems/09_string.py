'''Write a Python program to remove the nth index character from a nonempty string.'''

# def remove(str,n):
#     first_part = str[:n]
#     print(first_part)
#     last_part = str[n+1:]
#     print(last_part)
#     return first_part + last_part

def remove(str,n):
    for i in range(len(str)):
        if i==n:
            str = str.replace(str[i],"",1)
    return str        


print(remove('python is a very good',3))  
