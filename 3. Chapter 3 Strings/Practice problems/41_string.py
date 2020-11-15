'''Random Problem 1: alternate char lower upper
Sample Input
chris alan
Sample Output
ChRiS AlAn
'''
word = input()
def farrange(word):
    s1 = ""
    for i in range(0,len(word)):
        if i%2==0:
            s1= s1 + word[i].upper()
        else:
            s1= s1 + word[i].lower()
    return s1

print(farrange(word))









