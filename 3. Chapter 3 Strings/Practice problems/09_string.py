'''Write a Python program to remove the nth index character from a nonempty string.'''

def remove(str,n):
    first_part = str[:n]
    second_part = str[n+1:]
    return first_part+second_part

# def remove(str,n):
#     for i in range(len(str)):
#         if i==n:
#             str = str.replace(str[i],"")
#     return str


print(remove('python is a very good',3))  
