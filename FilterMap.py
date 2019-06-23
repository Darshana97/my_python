
'''def is_even(n):
    return n%2==0

nums = [1,2,3,4,5,6,7,8,9,10]

evens = list(filter(is_even,nums))

print(evens)'''

from functools import reduce

def add_all(a,b):
    return a+b

nums = [3,2,6,8,4,6,2,9]

evens = list(filter(lambda n: n%2==0,nums))

doubles = list(map(lambda n: n*2,evens))

sum = reduce(add_all,doubles)

print(evens)
print(doubles)
print(sum)

