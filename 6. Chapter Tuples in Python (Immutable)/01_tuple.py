'''Different types of tuple'''

my_tuple= ()
print(my_tuple)

# Tuple having integers
my_tuple = (1, 2, 3)
print(my_tuple)

# tuple with mixed datatypes
my_tuple = (1, "Hello", 3.4)
print(my_tuple)

# nested tuple
my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
print(my_tuple)

# my_tuple = 3, 4.6, "dog"
# print(my_tuple)
aTuple = (10, 20, 30, 40)


# tuple unpacking is also possible
a, b, c = my_tuple
a, b, c, d = aTuple

print(a)   #10    # 3
print(b)   #20    # 4.6
print(c)   #30    # dog
print(d)   #40

'''Creating a tuple with one element is a bit tricky.
Having one element within parentheses is not enough. 
We will need a trailing comma to indicate that it is, in fact, a tuple.'''

my_tuple = ("hello")
print(type(my_tuple))  # <class 'str'>

# Creating a tuple having one element
my_tuple = ("hello",)
print(type(my_tuple))  # <class 'tuple'>

# Parentheses is optional
my_tuple = "hello",
print(type(my_tuple))  # <class 'tuple'>

#Likewise, nested tuples are accessed using nested indexing, as shown in the example below.

# Accessing tuple elements using indexing
my_tuple = ('p','e','r','m','i','t')

print(my_tuple[0])   # 'p'
print(my_tuple[5])   # 't'

# IndexError: list index out of range
#print(my_tuple[6])

# Index must be an integer
# TypeError: list indices must be integers, not float
# my_tuple[2.0]

# nested tuple
n_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
aTuple = ("Orange", [10, 20, 30], (5, 15, 25))

# nested index
print(n_tuple[0][3])       # 's'
print(n_tuple[1][1])       # 4
print(aTuple[1][1])       # 20
# Negative Indexing
print(n_tuple[-1][2])

#Slicing
# Accessing tuple elements using slicing
my_tuple = ('p','r','o','g','r','a','m','i','z')

# elements 2nd to 4th
# Output: ('r', 'o', 'g')
print(my_tuple[1:4])

# elements beginning to 2nd
# Output: ('p', 'r')
print(my_tuple[:-7])

# elements 8th to end
# Output: ('i', 'z')
print(my_tuple[7:])

# elements beginning to end
# Output: ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')
print(my_tuple[:])

