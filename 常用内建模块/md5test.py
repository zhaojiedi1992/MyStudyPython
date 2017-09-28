import hashlib
md5 = hashlib.md5()
md5.update("how to user md 5 in hashlib".encode(encoding='utf_8'))
print(md5.hexdigest())