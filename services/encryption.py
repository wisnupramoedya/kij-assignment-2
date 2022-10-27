from Crypto.Cipher import ARC4
from Crypto.Hash import SHA

nonce = b"\x1aB!}\xc6Z8J\xce\x00\xc7\xdd\x9ag\x1e\xd1"


class Encryption:
    @staticmethod
    def get_cipher(key: bytes, nonce: bytes) -> ARC4:
        temp_key = SHA.new(key + nonce).digest()
        return ARC4.new(temp_key)

    @staticmethod
    def encrypt(data: bytes, key: bytes) -> bytes:
        cipher = Encryption.get_cipher(key, nonce)
        return nonce + cipher.encrypt(data)

    @staticmethod
    def decrypt(data: bytes, key: bytes) -> bytes:
        cipher = Encryption.get_cipher(key, data[:16])
        return cipher.decrypt(data[16:])


key = "Very long and confidential key".encode()
plain_text = "Hello Signing".encode()

print(plain_text)
cipher_text: bytes = Encryption.encrypt(plain_text, key)
print(cipher_text)
decrypted_text = Encryption.decrypt(cipher_text, key)
print(decrypted_text)
