
class Students:

    school = "Nugawela"

    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3


    def avg(self):
        return (self.m1+self.m2+self.m3)/3

    @classmethod
    def getSchool(cls):
        return cls.school

    @staticmethod
    def info():
        print("This is Student class...in abc molude")


s1 = Students(10,20,30)
s2 = Students(40,50,60)

print(s1.avg())
print(Students.getSchool())

Students.info()

