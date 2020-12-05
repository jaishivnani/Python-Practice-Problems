
class A:
    def feature1(self):
        print("Feature 1 is working")

    def feature2(self):
        print("Feature 2 is working")


# class B(A):  #Single Inheritance
class B:
    def feature3(self):
        print("Feature 1 is working")

    def feature4(self):
        print("Feature 2 is working")

# class C(B):  #Multi Level Inheritance
class C(A,B):  #Multiple Inheritance
    def feature5(self):
        print("Feature 1 is working")



a1 = A()
b1 = B()
c1 = C()


