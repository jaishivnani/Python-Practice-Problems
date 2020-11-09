'''Write a Python function to reverses a string if it's length is a multiple of 4. Go to the editor'''

def reverse_string(str):
    if len(str)%4==0:
        return str[::-1]
    else:
        return str

print(reverse_string("jai"))
print(reverse_string('abcd'))
print(reverse_string('python'))