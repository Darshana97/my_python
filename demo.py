
'''import calc

print("demo says:",__name__)'''

from calc import  *

def fun1():
    print("func1")
    add()

def fun2():
    print("func2")


def main():
    fun1()
    fun2()

main()