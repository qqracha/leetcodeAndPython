class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]  # каждый слот — это список

    def _hash(self, key):
        """Простейшая хэш-функция для строк и чисел"""
        if isinstance(key, int):
            return key % self.size
        elif isinstance(key, str):
            return sum(ord(char) for char in key) % self.size
        else:
            raise TypeError("Unsupported key type")

    def insert(self, key, value):
        """Вставка пары ключ-значение"""
        index = self._hash(key)
        # Проверяем, есть ли уже ключ, если есть — обновляем
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, value])

    def get(self, key):
        """Получение значения по ключу"""
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None  # если ключ не найден

    def delete(self, key):
        """Удаление ключа"""
        index = self._hash(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]
                return True
        return False

    def __str__(self):
        """Вывод хэш-таблицы"""
        result = ""
        for i, chain in enumerate(self.table):
            result += f"{i}: {chain}\n"
        return result


# Пример использования
ht = HashTable()

ht.insert("apple", 10)
ht.insert("banana", 20)
ht.insert("orange", 30)
ht.insert("grape", 40)
ht.insert("melon", 50)

print("Хэш-таблица после вставок:")
print(ht)

print("Получение значения по ключу 'banana':", ht.get("banana"))

ht.delete("orange")
print("Хэш-таблица после удаления 'orange':")
print(ht)
