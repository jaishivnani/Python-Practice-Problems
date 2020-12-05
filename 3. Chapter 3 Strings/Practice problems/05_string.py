'''Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string. Go to the editor
Sample String : 'abc', 'xyz'
Expected Result : 'xyc abz' '''

def charmixup(a,b):
    new_a = b[:2]+a[2:]
    new_b = a[:2]+b[2:]
    return new_a + " " + new_b

print(charmixup('abc','xyz'))