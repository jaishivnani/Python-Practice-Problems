'''Exercise Question 3:
Given 2 strings, s1, and s2 return a new string made of the first, middle and last char each input string
s1 = "America"
s2 = "Japan"
Sample Output
AJrpan
'''

def mix_string(s1,s2):
    first_char = s1[:1]+s2[:1]
    middleindexstr1 = int(len(s1)/2)
    middleindexstr2 = int(len(s2)/2)
    last_char = s1[-1:]+s2[-1:]
    print("Original String is ", s1, s2)
    finalstring = first_char+s1[middleindexstr1]+s2[middleindexstr2]+last_char
    print(finalstring)


mix_string("America","Japan")






