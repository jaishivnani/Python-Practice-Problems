'''Exercise Question : Concatenate two lists in the following order
['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']
'''

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

resList = [i+j for i in list1 for j in list2]

print(resList)
