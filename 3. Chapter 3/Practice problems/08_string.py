'''8. Write a Python function that takes a list of words and returns the length of the longest one.'''

def longest_string(word_list):
    word_len = []
    for n in word_list:
        word_len.append((len(n),n))
    word_len.sort()
    print(word_len)
    return word_len[-1][1]
   


print(longest_string(["PHP","PYTHON","JAVA"]))        