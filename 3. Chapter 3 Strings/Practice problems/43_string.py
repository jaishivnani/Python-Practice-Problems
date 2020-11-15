'''PyNative problem 2
Sample Input
s1 = "Ault"
s2 = "Kelly"
Sample Output
Dip
Son
'''

def getmiddlethreechars(s1,s2):
    middleindexstr1 = int(len(s1)/2)
    print("Original String is ",s1,s2)
    insertinmiddle = s1[:middleindexstr1]+s2+s1[middleindexstr1:]
    print(insertinmiddle)

getmiddlethreechars("Ault","Kelly")






