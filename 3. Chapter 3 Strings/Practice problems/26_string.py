'''Write a Python function to reverses a string'''

'''slice(start, stop, step)
Parameters:
start: Starting index where the slicing of object starts.
stop: Ending index where the slicing of object stops.
step: It is an optional argument that determines the increment between each index for slicing.'''

def reverse_string(str):
    return str[::-1]


print(reverse_string("jai"))
print(reverse_string('abcd'))
print(reverse_string('python Exercises'))

