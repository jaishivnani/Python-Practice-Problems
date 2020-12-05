av = 5

x = int(input("How many candies do you want:- "))

i = 1
while i<=x:

    if i>av:
        print("Out Of Stock")
        break
    print("Candy")
    i = i + 1

print("Bye")