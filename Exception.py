

a=5
b=4

try:
    print("resource open")
    print(a/b)
    k = int(input("enter value for k: "))
    print("k is: ",k)

except ZeroDivisionError as e:
    print("hey, you cannot divide a number by zero",e)


except ValueError as e:
    print("invalid input")

except Exception as e:
    print("something went wrong...")

finally:
    print("resoure closed")





