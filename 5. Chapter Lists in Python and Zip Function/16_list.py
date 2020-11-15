''' Given a Python list, multiply all numbers.
list1 = [5, 20, 15, 20, 25, 50, 20]
Expected output:
result=750000000
'''
# list1 = [5, 20, 15, 20, 25, 50, 20]

def mutiply_list(list1):
    result = 1
    for i in list1:
        result *= i
    return result

print(mutiply_list([5, 20, 15, 20, 25, 50, 20]))

