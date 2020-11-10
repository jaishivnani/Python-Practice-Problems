'''Formatting of Strings:- Strings in Python can be formatted with the use of format() method
which is very versatile and powerful tool for formatting of Strings.
Format method in String contains curly braces {} as placeholders which can hold arguments
according to position or keyword to specify the order.'''

'''Default Order'''
String1 = "{} {} {}".format('Geeks', 'For', 'Life')
print(String1)

'''Positional Formatting'''
String1 = "{1} {0} {2}".format('Geeks', 'For', 'Life')
print(String1)

'''Keyword Formatting'''
String1 = "{l} {f} {g}".format(g='Geeks', f='For',l='Life')
print(String1)
