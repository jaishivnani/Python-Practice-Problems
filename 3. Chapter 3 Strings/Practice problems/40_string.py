'''Hackerank Problem 8: Capitalize
Sample Input
chris alan
Sample Output
Chris Alan
'''
# !/bin/python3

import math
import os
import random
import re
import sys


# Complete the solve function below.
def solve(s):
    l = s.split(" ")
    s = ''
    for i in range(l):
        s = s + i.capitalize() + ' '
    print(s)


if __name__ == '__main__':
    s = input()
    result = solve(s)



