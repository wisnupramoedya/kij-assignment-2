from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA


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

