from cryptography.fernet import Fernet

'''def generate_key():
    key = Fernet.generate_key()
    #print(key)
    with open("key.key", "wb") as f:
        f.write(key)
        '''
    
with open("key.key", "rb") as mykey:
    key = mykey.read()

print(key)
f = Fernet(key)

with open("elias.txt", "rb") as original_file:
    original = original_file.read()

encrypted_file = f.encrypt(original)

with open("elas_encrypted.txt", "wb") as encrypted:
    encrypted.write(encrypted_file)


#f = Fernet(key)
with open("elas_encrypted.txt", "rb") as encrypted:
    encryptedme= encrypted.read()
    
decrypted_file = f.decrypt(encryptedme)
with open("elas_decrypted.txt", "wb") as decrypted:
    decrypted.write(decrypted_file)
