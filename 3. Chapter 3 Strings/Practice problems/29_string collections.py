'''Write a Python program to count repeated characters in a string.
Sample string: 'thequickbrownfoxjumpsoverthelazydog'''

# sorted(iterable, key=key, reverse=reverse)
# Parameter Values
# Parameter|Description
# iterable |Required. The sequence to sort, list, dictionary, tuple etc.
# key	   |Optional. A Function to execute to decide the order. Default is None
# reverse  |Optional. A Boolean. False will sort ascending, True will sort descending. Default is False
import collections
str= 'thequickbrownfoxjumpsoverthelazydog'

d = collections.defaultdict(int)

for c in str:
    d[c]+=1

for c in sorted(d,key=d.get,reverse=True):
    if d[c]>1:
        print("%s %d"%(c,d[c]))