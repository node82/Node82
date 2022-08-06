import hashlib
string = 'YOUR_PASSWORD'
hashedString = hashlib.sha256(string.encode('utf-8')).hexdigest()
print(hashedString)
