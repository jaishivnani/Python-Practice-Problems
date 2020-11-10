'''Write a Python program to strip a set of characters from a string.'''

def strip_chars(str,chars):
    return "".join(ch for ch in str if ch not in chars)

print(strip_chars("The quick brown fox jumps over the lazy dog.","aeiou"))



