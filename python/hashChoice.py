import hashlib
import pyperclip
hashThis = input("What do You Want To hash?\n")
hashChoice = input("what flavor : 1. sha224 | 2. sha256 | 3. sha384 | 4. sha512 | 5. blake2b | 6. blake2s | 7. shake128 | 8. shake256?")
if hashChoice == "1":
    hashedString = hashlib.sha224(hashThis.encode('utf-8')).hexdigest()
if hashChoice == "2":
    hashedString = hashlib.sha256(hashThis.encode('utf-8')).hexdigest()
if hashChoice == "3":
    hashedString = hashlib.sha384(hashThis.encode('utf-8')).hexdigest()
if hashChoice == "4":
    hashedString = hashlib.sha512(hashThis.encode('utf-8')).hexdigest()
if hashChoice == "5":
    hashedString = hashlib.blake2b(hashThis.encode('utf-8')).hexdigest()
if hashChoice == "6":
    hashedString = hashlib.blake2s(hashThis.encode('utf-8')).hexdigest()
if hashChoice == "7":
    hashedString = hashlib.shake128(hashThis.encode('utf-8')).hexdigest()
if hashChoice == "8":
    hashedString = hashlib.shake256(hashThis.encode('utf-8')).hexdigest()
else:
    print("something else was selected, i'm disappointed")
    hashChoice = input("what flavor : 1. sha224 | 2. sha256 | 3. sha384 | 4. sha512 | 5. blake2b | 6. blake2s | 7. shake128 | 8. shake256?")
print(hashedString)
pyperclip.copy(hashedString)
print("has been copied to your clipboard, use it wisely")
