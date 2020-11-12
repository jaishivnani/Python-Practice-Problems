'''Hackerank Problem 4: Mutations
Sample Input String="abracadabra"
mutable_string(abracadabra,10,k)
sample Output String = "abracadabrk"
'''

def mutate_string(string,position,character):
    string = string[:position]+"%s"%character+ string[position+1:]
    return string


if __name__ == '__main__':
    s= input()
    i,c=input().split()
    s_new=mutate_string(s,int(i),c)
    print(s_new)
