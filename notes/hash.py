import hashlib

pswrd = "rogen".encode()
hash_object = hashlib.sha256(pswrd)

print(hash_object) # class object sha256 hashing
print(hash_object.hexdigest()) # hash output