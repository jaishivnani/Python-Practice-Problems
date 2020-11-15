''' Given a Python list, Max of list
list1 = [5, 20, 15, 20, 25, 50, 20]
Expected output:
MAX = 50
'''
# list1 = [5, 20, 15, 20, 25, 50, 20]

def max_num_in_list(list):
    max  =list[0]
    for i in list:
        if i>max:
            max=i
    return max

print(max_num_in_list([5, 20, 15, 20, 25, 50, 20]))

