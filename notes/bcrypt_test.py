import bcrypt

pswrd = b"rogen" # b - bytes type 
hashed = bcrypt.hashpw(pswrd, bcrypt.gensalt())
print(hashed)