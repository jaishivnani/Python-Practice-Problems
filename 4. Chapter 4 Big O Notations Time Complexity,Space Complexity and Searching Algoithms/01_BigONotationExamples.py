'''Big O Notation Example 1 - Square of list of numbers'''

# numbers = [2,5,8,9]
#
# def get_squared_numbers(numbers):
#     squared_numbers=[]
#     for n in numbers:
#         squared_numbers.append(n*n)
#     return squared_numbers
#
# print(get_squared_numbers([2,5,8,9]))

# Time Complexity:- f(n) = 2n+2 = O(n)

'''Big O Notation Example 2 - Stock Calculation'''

# def find_first_pe(prices,eps,index):
#     pe = prices[index]/eps[index]
#     return pe

# Time Complexity:- f(n) = O(1)

'''Big O Notation Example 3 Finding duplicate numbers in List'''
list_numbers = [3,6,2,4,3,6,8,9]

for i in range(len(list_numbers)):
    for j in range(i+1,len(list_numbers)):
        if list_numbers[i]==list_numbers[j]:
            list_numbers.remove(list_numbers[i])
            print(list_numbers[i],"is a duplicate")
            break

# Time Complexity:- f(n) = 2n^2+n+2 = O(n^2)






