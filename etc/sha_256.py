from hashlib import sha256

s = input()
result = sha256(s.encode()).hexdigest()
print(result)