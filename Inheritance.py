
class A:

    def feature1(self):
        print("feature 1")

    def feature2(self):
        print("feature 2")



class B:

    def feature3(self):
        print("feature 3")

    def feature4(self):
        print("feature 4")


class C(A,B):

    def feature5(self):
        print("feature 5")



a1 = A()
b1 = B()
c1 = C()


a1.feature1()
c1.feature1()
