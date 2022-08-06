import hashlib
import pyperclip
hashThis = input("What do You Want To hash?\n")
hashedString = hashlib.sha256(hashThis.encode('utf-8')).hexdigest()
print(hashedString)
pyperclip.copy(hashedString)
print("has been copied to your clipboard, use it wisely")
