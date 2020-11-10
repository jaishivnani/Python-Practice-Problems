'''Write a Python program to Split and then again join the Sentence of a String.'''
'''Splitting Sentence'''

def splitUpSentence(str1):
    return str1.split()

splitUp = splitUpSentence("The quick brown fox jumps over the lazy dog.")
print("The Splitup Sentence is:",splitUp)

'''Joining Sentence'''
'''Joining Sentence again by passing the output of SplitUp Sentence.'''

def joinSplitUpSentence(str1):
    return " ".join(splitUp)

print("The Joined Sentence is:",joinSplitUpSentence(splitUp))