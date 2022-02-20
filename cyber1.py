from cryptography.fernet import Fernet

key = Fernet.generate_key()
Fernet.
print (key)
cyber_suite = Fernet(key)

encrpted_text = cyber_suite.encrypt(b'Hello')

print(encrpted_text)

decypted_text = cyber_suite.decrypt(encrpted_text)

print(decypted_text)

