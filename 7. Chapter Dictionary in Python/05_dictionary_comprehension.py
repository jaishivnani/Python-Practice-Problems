# dict1 = {0:"item1",1:"item1"}
# we will do above thing by using comprehensions
# dict1 = {i:f"Item{i}" for i  in range(1,10000) if i%100==0}

'''Python Dictionary Comprehension'''
# Dictionary Comprehension
squares = {x: x*x for x in range(6)}
print(squares)

#Above Program with For Loop
squares = {}
for x in range(6):
    squares[x] = x*x
print(squares)

# Dictionary Comprehension with if conditional
odd_squares = {x: x*x for x in range(11) if x % 2 == 1}
print(odd_squares)


dict1 = {i:f"Item {i}" for i  in range(5)}

dict2 = {value:key for key,value in dict1.items()}
print(dict1,"\n",dict2)
