def greet(*args):
    print(args)

greet("i", "wanna", "pizza")

def my_sum(*args):
    return sum(args)

print(my_sum(1, 2))           # 3
print(my_sum(1, 2, 3, 4, 5))  # 15


def info(**kwargs):
    print(kwargs)

info(name = "Даша", age = 20)