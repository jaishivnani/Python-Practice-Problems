'''dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}'''

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

#Python 3.5 and higher
# dict3 = {**dict1,**dict2}
# print(dict3)

def Merge(d1, d2):
    d1.update(d2)

Merge(dict1,dict2)
print(dict1)