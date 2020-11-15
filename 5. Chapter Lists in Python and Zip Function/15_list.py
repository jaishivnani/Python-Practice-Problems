''' Given a Python list, print sum
list1 = [5, 20, 15, 20, 25, 50, 20]
Expected output:
sum =
'''
list1 = [5, 20, 15, 20, 25, 50, 20]

def sum_list(lst):
    sum_numbers=0
    for x in lst:
        sum_numbers += x
    return sum_numbers

print(sum_list(list1))

