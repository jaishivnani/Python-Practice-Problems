'''Python List questions'''

'''1.Lists Definition:- Lists are one of the four built-in data structures in Python, together with tuples, 
dictionaries, and sets. They are used to store an ordered collection of items, which might be of different 
types but usually they aren’t.Commas separate the elements that are contained within a list and enclosed in
 square brackets.'''

'''2.Lists Vs Tuples:- Tuples are used to collect an immutable ordered list of elements. 
This means that:
1. You can’t add elements to a tuple. There’s no append() or extend() method for tuples.
2. You can’t remove elements from a tuple. Tuples have no remove() or pop() method.
3. You can find elements in a tuple since this doesn’t change the tuple.
4. You can also use the in operator to check if an element exists in the tuple.
So, if you’re defining a constant set of values and all you’re going to do with it is iterate through it, 
use a tuple instead of a list. It will be faster than working with lists and also safer
as the tuples contain “write-protect” data.
They are used to store an ordered collection of items, which might be of different 
types but usually they aren’t.Commas separate the elements that are contained within a list and enclosed in
 square brackets.'''

'''3.Lists Versus Dictionaries
1.A list stores an ordered collection of items, so it keeps some order. Dictionaries don’t have any order.
2.Dictionaries are known to associate each key with a value, while lists just contain values.
3.Use a dictionary when you have an unordered set of unique keys that map to values.
4.Note that, because you have keys and values that link to each other, 
the performance will be better than lists in cases where you’re checking membership of an element.
'''

'''Lists Versus Sets
1.Just like dictionaries, sets have no order in their collection of items. Not like lists.
2.Set requires the items contained in it to be hashable, lists store non-hashable items.
3.Sets require your items to be unique and immutable. 
Duplicates are not allowed in sets, while lists allow for duplicates and are mutable.

You should make use of sets when you have an unordered set of unique, immutable values that are hashable.'''



'''Hashable	     Non-Hashable
   Floats	     Dictionaries
   Integers	     Sets
   Tuples	     Lists
   Strings
   frozenset()                    '''
