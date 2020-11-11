n = int(input("Enter the number which you need to search:- "))
list = [5,8,4,6,9,2]
pos = -1
def linearsearch(list,n):     # Creating method which will take list and no which need to search as input.

   for i in range (len(list)):           # To traverse the list.
        if list[i]==n:                   # To check if index value i is equal to value we are searching.
            globals()['pos']= i          # Accessing global variable pos locally and assigning the value of i to it.
            return True



found = linearsearch(list,n)  # Calling method or function and storing the boolean value returned in found variable.


if linearsearch(list,n):
    print(found,'Found at',pos+1)
else:
    print('Not Found')

# Time Complexity:- f(n) = 6n+3 = O(n)