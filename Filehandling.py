
f = open('MyData','r')
print(f.read())




f1 = open("abc","w")
#f1.write("i am buddhist and i'm proud to say that")

for data in f:
    f1.write(data)

