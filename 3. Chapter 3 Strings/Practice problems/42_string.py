'''PyNative problem 1
Sample Input
str1 = "JhonDipPeta"
str2 = "JaSonAy"
Sample Output
Dip
Son
'''

def getmiddlethreechars(str):
    middleindex = int(len(str)/2)
    print(middleindex)
    print("Original String is ",str)
    middlethree = str[middleindex-1:middleindex+2]
    print(middleindex-1,middleindex+2)
    print("Middle three chars are",middlethree)

getmiddlethreechars("JhonDipPeta")
getmiddlethreechars("JaSonAy")






