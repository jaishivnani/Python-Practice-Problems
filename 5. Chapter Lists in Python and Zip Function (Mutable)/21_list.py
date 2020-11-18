''' Write a Python program to remove duplicates from a list.
Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples. Go to the editor
Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
'''

# sampleList = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

# def last(n): return n[-1]
#
# def sort_list_last(tuples):
#   return sorted(tuples, key=last)
#
# print(sort_list_last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))


def empty_lst_or_not(a):
  return 'list is empty' if len(a) == 0 else 'list is not empty'

x = []
print(empty_lst_or_not([]))




