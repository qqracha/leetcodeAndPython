s = [1,2,3,4,5,6,15,7,8]
strigTest = "goofyAH"
stringTest_copy = strigTest # хэши будут одинаковыми

print(s[:2]) # [0,1]
print(s[2:]) # [2,3,4,5,6,15,7,8]
print(s[2:5]) # [3,4,5]
print(s.index(15)) # 6
print(s.count(5))

print(hash(strigTest))
print(hash(stringTest_copy))

s.extend(["cucumber", "tomato"]) # [1, 2, 3, 4, 5, 6, 15, 7, 8, 'cucumber', 'tomato']
print(s)

s.insert(3, "pencil") # [1, 2, 3, 'pencil', 4, 5, 6, 15, 7, 8, 'cucumber', 'tomato']        
print(s)
print(strigTest.encode)