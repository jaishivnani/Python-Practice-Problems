'''Similarly, we can remove and return an item using the pop() method.
Since set is an unordered data type,
there is no way of determining which item will be popped. It is completely arbitrary.
We can also remove all the items from a set using the clear() method.'''

# initialize my_set
# Output: set of unique elements
my_set = set("HelloWorld")
print(my_set)

# pop an element
# Output: random element
print(my_set.pop())

# pop another element
my_set.pop()
print(my_set)

# clear my_set
# Output: set()
my_set.clear()
print(my_set)
