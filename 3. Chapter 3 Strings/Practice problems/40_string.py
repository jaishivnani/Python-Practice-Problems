'''Hackerank Problem 8: Capitalize
Sample Input
chris alan
Sample Output
Chris Alan
'''

def capfrstletter(words):
    list = words.split(" ")
    s = ''
    for i in list:
        s = s + i.capitalize() + ' '

    return s


if __name__ == '__main__':
    s = input()
    result = capfrstletter(s)
    print(result)



