import uuid
import clipboard
hash = str(uuid.uuid1())
clipboard.copy(hash)
print (hash)
