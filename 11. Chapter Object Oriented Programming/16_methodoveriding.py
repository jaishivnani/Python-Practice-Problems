class A:

    def show(self):
        print("In A show")

class B(A):
#pass-The moment you add show method in B it will stop overiding show method from A and will call its own show method.

    def show(self):
        print("In B show")



a1 = B()

a1.show()