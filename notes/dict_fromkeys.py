words = ["apple", "banana", "cherry"]
vals = [1, 2, 3]
d = dict.fromkeys(words, 95)   # all keys have 95 value
for key, value in d.items():
    print(key, value)

d.values()
print(d)

print(dict(zip(words, vals)))