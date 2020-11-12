'''Hackerank Problem 2 String Split and Join'''

# Input String :-  a = "this is a string"

def split_and_join(line):
    a = line.split()
    a="-".join(a)
    return a

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)





