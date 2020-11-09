'''Write a Python function that takes a list of words and returns the length of the longest one.'''

def longest_word(word_list):
    word_len=[]
    for n in word_list:
        word_len.append((len(n),n))
    word_len.sort()
    return word_len[-1][1]

print(longest_word(["PHP","PYTHON","JAVA"]))

# Time Complexity = 2n+3