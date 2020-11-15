'''Exercise Question 4:
Count all lower case, upper case, digits, and special symbols from a given string
Given str1 = "P@#yn26at^&i5ve"
Total counts of chars, digits,and symbols

Chars = 8
Digits = 3
Symbol = 4
'''

str1 = "P@#yn26at^&i5ve"
def lowerfirst(str1):
    charcount = 0
    digitcount = 0
    symbolcount = 0
    for char in str1:
        if char.isalpha():
            charcount = charcount+1
        elif char.isdigit():
            digitcount = digitcount+1
        else:
            symbolcount=symbolcount+1

    print("Character Count:",charcount,"Digit Count:",digitcount,"Symbol Count:",symbolcount)



lowerfirst(str1)










