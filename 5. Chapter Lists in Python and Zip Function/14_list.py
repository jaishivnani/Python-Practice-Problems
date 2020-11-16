''' Given a Python list, remove all occurences of 20 in the list
list1 = [5, 20, 15, 20, 25, 50, 20]
Expected output:
list1 = [5, 15, 25, 50]
'''

list1 = [5, 20, 15, 20, 25, 50, 20]

def removevalue(sampleList,val):
    return [value for value in sampleList if value!=val]

resList = removevalue(list1,20)
print(resList)

