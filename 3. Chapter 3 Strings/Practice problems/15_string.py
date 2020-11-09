'''Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form (alphanumerically). Go to the editor
Sample Words : red, red, white, black, red, green, black, white
Expected Result : black, green, red, white, red'''

words=input("Input comma separated words:-")

word = [word for word in words.split(",")]
print(",".join(sorted(list(set(word)))))

