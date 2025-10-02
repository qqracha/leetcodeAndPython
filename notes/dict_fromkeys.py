words = ["apple", "banana", "cherry"]
d = dict.fromkeys(words, 95)   # all keys have 95 value
for key, value in d.items():
    print(key, value)

d.popitem()
print(d)