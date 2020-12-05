'''If A and B are two sets.
The set difference of A and B is a set of elements that exists only in set A but not in B.'''


set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

set1.difference_update(set2)
print(set1)
# output {40, 50, 30}