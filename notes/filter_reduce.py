from functools import reduce

numbers = [5,1,7,4,2,6,3,8]

print(list(filter(lambda x: x % 2 == 0, numbers)))
print(reduce(lambda x, y: x * y, numbers))