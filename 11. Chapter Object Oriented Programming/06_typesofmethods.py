
class Student:

    school = "Telusko"
# ----------------Instance Methods - If you are working with instance methods you will be using self keyword---------------------------------------------------------------#
    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1+self.m2+self.m3)/3

    def get_m1(self):
        return self.m1            #Accessor methods

    def set_m1(self,value):
        self.m1 = value           #Mutator methods

# ----------------Class Methods - If you are working with class methods you will be using cls keyword---------------------------------------------------------------#
    @classmethod
    def getSchool(cls):
        return cls.school

#Static Methods - This method is nothing to do with instance and class variables (Self and cls) If you are working with other class objects you will use static methods.---------------------------------------------------------------#
    @staticmethod
    def info():
        print("This is Student Class")

s1 = Student(34,67,32)
s2 = Student(89,12,98)

print(s1.avg())
print(s2.avg())
print(Student.getSchool())
Student.info()





