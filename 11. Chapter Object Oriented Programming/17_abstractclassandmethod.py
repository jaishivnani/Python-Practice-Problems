from abc import ABC,abstractmethod

class Computer(ABC):      #Classes which have abstract methods is abstract classes.
    @abstractmethod
    def process(self):
        pass              #The methods which only has declaration but not a defination is called abstract method.

class Laptop(Computer):
    def process(self):
        print("its running")

class Desktop(Computer):          #Implementing or inheriting abstract class and abstract method process because Desktop
    def process(self):            #is inheriting abstract class Computer.
        print("its loading")

class Programmer:
    def work(self,com):
        print("solving bugs")      #Passing object of Laptop to Programmer
        com.process()

class Whiteboard:
    def write(self):
        print("its writing")   #It is not compulsary for whiteboard to have a method process but if you say whiteboard
                               #is as computer it becomes compulsion


# com = Computer()  we cannot create object of abstract class
com1 = Laptop()
# com1.process()
com2 = Desktop()
com3 = Whiteboard()
prog1 = Programmer()
prog1.work(com1)
prog1.work(com2)
# prog1.work(com3)   #'Whiteboard' object has no attribute 'process'
