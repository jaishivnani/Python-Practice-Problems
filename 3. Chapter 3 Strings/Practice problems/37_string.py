'''Hackerank Problem 5: Find a string
Sample Input
ABCDCDC
CDC
Sample Output
2
'''

def count_substring(string,sub_string):
    count = 0
    for i in range(len(string)):
        if string[i:].startswith(sub_string):
            count+=1
    return count

if __name__ == '__main__':
    string = input()
    sub_string = input()
    count = count_substring(string,sub_string)
    print(count)