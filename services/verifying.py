import os

from Crypto.PublicKey import RSA
from Crypto.Signature.pkcs1_15 import PKCS115_SigScheme
from services.hashing import Hashing
from constants.mode import *


class Verifying:
    @staticmethod
    def verify(path_file: str, path_key: str):
        if not Verifying.detach_pdf(path_file):
            try:
                os.remove('original_file.pdf')
            finally:
                return SIGNATURE_NOT_FOUND
        f = open("digital_signature.txt", "br")
        digital_signature = f.read()
        original_hash = Hashing.hash_sha256('original_file.pdf')
        digital_signature = digital_signature.decode()
        try:
            key = open(path_key, 'r')
            PKCS115_SigScheme(RSA.import_key(key.read())).verify(original_hash, bytes.fromhex(digital_signature))
            key.close()
            return SIGNATURE_MATCH
        except ValueError:
            return SIGNATURE_NOT_MATCH
        finally:
            f.close()
            os.remove('digital_signature.txt')
            os.remove('original_file.pdf')

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
