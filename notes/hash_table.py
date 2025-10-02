class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]  # каждый слот — список (цепочка)

    def _hash(self, key):
        """Хэшируем с помощью встроенной функции hash()"""
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        # проверяем, есть ли ключ
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value  # обновляем
                return
        self.table[index].append([key, value])  # вставляем новый

    def get(self, key):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None

    def delete(self, key):
        index = self._hash(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]
                return True
        return False

    def __str__(self):
        result = ""
        for i, chain in enumerate(self.table):
            result += f"{i}: {chain}\n"
        return result


# Пример использования
ht = HashTable(size=5)  # маленький размер, чтобы увидеть коллизии

ht.insert("apple", 10)
ht.insert("banana", 20)
ht.insert("orange", 30)
ht.insert("grape", 40)
ht.insert("melon", 50)

print("Хэш-таблица после вставок:")
print(ht)

print("Значение по ключу 'banana':", ht.get("banana"))

ht.delete("orange")
print("После удаления 'orange':")
print(ht)
