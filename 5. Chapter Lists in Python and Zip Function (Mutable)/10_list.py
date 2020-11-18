''' list1 = [5, 20, 15, 20, 25, 50, 20]
           for x in list1:
                  if x == 20:
                       list1.remove(20)
           print(list1)'''

list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
list1 =[x for x in list1 if not x==""]
#
# for x in list1:
#     if x=="":
#         list1.remove("")
print(list1)