import fitz
import os

from hashing import Hashing
from encryption import Encryption

class Verifying:
    @staticmethod
    def verify(path_file: str, path_key: str):
        Verifying.detach_pdf(path_file)
        f = open("digital_signature.txt", "br")
        digital_signature = f.read()
        print(digital_signature.decode())

        signature_hash = Encryption.decrypt(data=bytes.fromhex(digital_signature.decode()), key_filepath=path_key)
        original_hash = Hashing.hash_sha256('original_file.pdf')
        # print(original_hash)
        # print(signature_hash)
        f.close()
        os.remove('digital_signature.txt')
        os.remove('original_file.pdf')
        if signature_hash == original_hash:
            return True
        else:
            return False

    @staticmethod
    def detach_pdf(filepath: str):
        data = b''
        with open(filepath, 'br') as fp:
            lines = fp.readlines()
            for idx, line in enumerate(lines):
                if line.__contains__(b'/Key /Contents'):
                    with open('digital_signature.txt', 'wb') as f_ds:
                        ds = line.split(b'/Contents<')
                        f_ds.write(ds[1][:-5])
                else:
                    data = data + line
            with open('original_file.pdf', 'wb') as f_ori:
                f_ori.write(data)


print(Verifying.verify(path_file="testcase/Ethereum-Whitepaper.pdf", path_key="testcase/test-private-key.pem"))
