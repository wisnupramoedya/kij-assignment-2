import codecs

from hashing import Hashing
from encryption import Encryption


class Signing:
    @staticmethod
    def get_digital_signature(self, path_file: str, path_key: str) -> bytes:
        hashed_data = Hashing.hash_sha256(path_file=path_file)
        digital_signature = Encryption.encrypt(data=hashed_data, key_filepath=path_key)
        return codecs.encode(digital_signature, 'hex')

    def sign(self, path_file: str, path_key: str):
        # attach_pdf(path_file, self.get_digital_signature(path_file=path_file, key=path_key))
        pass

    def attach_pdf(self, path_file: str, digital_signature: bytes):
        pass


sign = Signing.get_digital_signature("../testcase/test-paper.pdf", "Very long and confidential key".encode())
print(sign)
