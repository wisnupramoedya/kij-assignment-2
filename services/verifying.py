import os

from services.hashing import Hashing
from services.encryption import Encryption
from constants.mode import *


class Verifying:
    @staticmethod
    def verify(path_file: str, path_key: str):
        if not Verifying.detach_pdf(path_file):
            return SIGNATURE_NOT_FOUND
        f = open("digital_signature.txt", "br")
        digital_signature = f.read()

        try:
            signature_hash = Encryption.decrypt(data=bytes.fromhex(digital_signature.decode()), key_filepath=path_key)
        except ValueError:
            return SIGNATURE_NOT_MATCH

        original_hash = Hashing.hash_sha256('original_file.pdf')
        f.close()
        os.remove('digital_signature.txt')
        os.remove('original_file.pdf')
        if signature_hash == original_hash:
            return SIGNATURE_MATCH
        else:
            return SIGNATURE_NOT_MATCH

    @staticmethod
    def detach_pdf(filepath: str) -> bool:
        is_found_content = False
        data = b''
        with open(filepath, 'br') as fp:
            lines = fp.readlines()
            for idx, line in enumerate(lines):
                if line.__contains__(b'/Key /Contents'):
                    is_found_content = True
                    with open('digital_signature.txt', 'wb') as f_ds:
                        ds = line.split(b'/Contents<')
                        f_ds.write(ds[1][:-5])
                else:
                    data = data + line

            if not is_found_content:
                return False

            with open('original_file.pdf', 'wb') as f_ori:
                f_ori.write(data)
            return True

# print(Verifying.verify(path_file="testcase/Ethereum-Whitepaper.pdf", path_key="testcase/test-private-key.pem"))
