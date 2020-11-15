''' Given a Python list, Min of list
list1 = [5, 20, 15, 20, 25, 50, 20]
Expected output:
MIN = 5
'''
# list1 = [5, 20, 15, 20, 25, 50, 20]

def min_num_in_list(list):
    min  =list[0]
    for i in list:
        if i<min:
            min=i
    return min

print(min_num_in_list([5, 20, 15, 20, 25, 50, 20]))

