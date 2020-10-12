'''Write a Python program to count the number of characters (character frequency) in a string.'''

def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word]+=1
        else:
            counts[word]=1

    return counts


print(word_count("Python is is very simple and user friendly language."))

