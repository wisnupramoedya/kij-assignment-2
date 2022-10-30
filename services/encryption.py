from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

nonce = b"\x1aB!}\xc6Z8J\xce\x00\xc7\xdd\x9ag\x1e\xd1"


class Encryption:
    @staticmethod
    def get_cipher(key_filepath: str) -> PKCS1_OAEP:
        key = RSA.importKey(open(key_filepath).read())
        return PKCS1_OAEP.new(key)

    @staticmethod
    def encrypt(data: bytes, key_filepath: str) -> bytes:
        cipher = Encryption.get_cipher(key_filepath)
        return cipher.encrypt(data)

    @staticmethod
    def decrypt(data: bytes, key_filepath: str) -> bytes:
        cipher = Encryption.get_cipher(key_filepath)
        return cipher.decrypt(data)


public_key_filepath = "E:\Sekolah\Tugas Kuliah\Semester 7\KIJ\Assignment 2\sign-and-verif-app\\testcase\\test-public-key.pem"
private_key_filepath = "E:\Sekolah\Tugas Kuliah\Semester 7\KIJ\Assignment 2\sign-and-verif-app\\testcase\\test-private-key.pem"
plain_text = "Hello Signing".encode()

print(plain_text)
cipher_text: bytes = Encryption.encrypt(plain_text, public_key_filepath)
print(cipher_text)
decrypted_text = Encryption.decrypt(cipher_text, private_key_filepath)
print(decrypted_text)
