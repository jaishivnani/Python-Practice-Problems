''' Write a Python program to remove duplicates from a list.
list_numbers = [3,6,2,4,3,6,8,9]
Expected output:
list_numbers = [6,2,4,3,6,8,9]
'''

a = [3,6,2,4,9,9,9,9]

def remove_duplicates(lst):
    unique_items = set()
    for x in lst:
        unique_items.add(x)
    print(list(unique_items))

remove_duplicates([3,3,6,6,6,2,4,9,9,9,9])



