'''Recursion Simple Example'''
# import sys
# sys.setrecursionlimit(2000)
# print(sys.getrecursionlimit())
# i = 0
# def greet():
#     global i
#     i+=1
#     print("Hello",i)
#     greet()                 #Recursion is Function calling itself.
#
# greet()

#Time Complexity = O(n)

'''Factorial using Recursion'''
def fact(n):
    if n == 1 or n == 0:
        return 1
    return n * fact(n - 1)

n = int(input('Enter the number for which you need to calculate factorial:-'))

result = fact(n)
print(result)

#Time Complexity = O(n)