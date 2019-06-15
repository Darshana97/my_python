
class A:

    def __init__(self):
        print("in init A")

    def feature1(self):
        print("in feature 1")

    def feature2(self):
        print("in feature 2")

class B:

    def __init__(self):
        super().__init__()
        print("in init B")

    def feature1(self):
        print("in feature 3")

    def feature4(self):
        print("in feature 4")

class C(A,B):

    def __init__(self):
        super().__init__()
        print("in init C")


#a1 = A()
b1 = C()
b1.feature1()


