x = [9,2,8,4,5,6]

# Итератор
class Enigma:
    def __init__(self, limit):
        self.limit = limit
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.limit:
            self.count += 1
            return self.count
        raise StopIteration

# Генератор
def rogen(limit):
    count = 1
    while count <= limit:
        yield count
        count += 1

enigma_test = Enigma(len(x))
for i in enigma_test:
    print(f"Элемент из списка: {x[i-1]}")

print("-"*20)

rogen_test = rogen(len(x))
for i in rogen_test:
    print(f"Скибоб: {x[i-1]}")

y = list(set(x))
print(y)