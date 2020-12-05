
class Computer:

    def __init__(self):
        self.name = "Navin"
        self.age = 30


    def update(self):
        self.age = 30

    def compare(self,other):
        if self.age == other.age:
            return True
        else:
            return False




c1 = Computer()
c1.age = 30
c1.name = "Rashi"
c2 = Computer()
c2.age = 30

if c1.compare(c2):
    print("They are Same")
else:
    print("They are different")



#c1.update()          #if you call update c1 would be passed on behalf of self and age of c1 will be updated

print(c1.name)
print(c2.name)
print(c1.age)
print(c2.age)