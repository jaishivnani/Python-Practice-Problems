''''''

# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}

# print(set1.intersection(set2))
#output {40, 50, 30}

# set1 = {10, 20, 30, 40, 50}
# set2 = {60, 70, 80, 90, 10}
#
# print(set1.intersection(set2))

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

set1.intersection_update(set2)
print(set1)
