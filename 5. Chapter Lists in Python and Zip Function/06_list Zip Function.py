'''Zip Function in Python'''
names = ["Naveen","Kiran","Harsh"]
companies = ["Dell","Apple","Microsoft"]

'''Printing zipped by for loop'''
# zipped = zip(names,companies)
# for a,b in zipped:
#     print(a,b)

'''Printing zipped by converting it to list, set, dictionary'''
# zipped = dict(zip(names,companies))
# zipped = list(zip(names,companies))
# zipped = tuple(zip(names,companies))
# print(zipped)

'''Exercise Question : Using Zip to Concatenate two lists index-wise'''

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

list3 =[i+j for i,j in zip(list1,list2)]
print(list3)