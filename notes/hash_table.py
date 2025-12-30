
text = "spam spam eggs spam"
freq = {}

for word in text.split():
    freq[word] = freq.get(word, 0) + 1

print(freq)  # {'spam': 3, 'eggs': 1}


### Свой ключ (важно: __hash__ + __eq__)
class UserId:
    def __init__(self, value: int):
        self.value = value

    def __hash__(self):
        return hash(self.value)

    def __eq__(self, other):
        return isinstance(other, UserId) and self.value == other.value


users = {}
users[UserId(1)] = "Alice"
users[UserId(2)] = "Bob"

print(users[UserId(1)])  # Alice