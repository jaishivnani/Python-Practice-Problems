'''Write a Python program to calculate the length of a string'''

'''Using in built Function'''

String = input("Enter the String:-" )
print(len(String))

'''Using Function'''
def string_length(str):
    count=0
    for char in str:
        count+=1
    return count


print(string_length(""))
# Time Complexity = 2n + 2 = O(n)






