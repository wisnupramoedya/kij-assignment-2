import codecs
import re
from Crypto.Signature.pkcs1_15 import PKCS115_SigScheme
from Crypto.PublicKey import RSA

from services.hashing import Hashing


class Signing:
    @staticmethod
    def get_digital_signature(path_file: str, path_key: str) -> str:
        hashed_data = Hashing.hash_sha256(path_file=path_file)
        f = open(path_key, 'r')
        digital_signature = PKCS115_SigScheme(RSA.import_key(f.read())).sign(hashed_data)
        hex_ds = codecs.encode(digital_signature, 'hex')
        str_ds = hex_ds.decode()
        return str_ds

    @staticmethod
    def sign(path_file: str, path_target: str, path_key: str) -> bool:
        is_attached = Signing.attach_pdf(path_file, path_target,
                                         Signing.get_digital_signature(path_file=path_file, path_key=path_key))
        if is_attached:
            return True
        else:
            return False

    @staticmethod
    def attach_pdf(filepath: str, path_target: str, digital_signature: str) -> bool:
        attachment = bytes(f'<</Key /Contents<{digital_signature}>>>\r\n', 'UTF-8')
        position = 0
        with open(filepath, 'br+') as fp:
            line = 0
            while True:
                test = fp.readline()
                if not test:
                    break
                line += 1
                if test.find(b'%%EOF') != -1:
                    position = line
            fp.seek(0)
            lines = fp.readlines()
            check_line = lines[position - 2]
            lines.append(lines[position - 1])
            lines[position - 1] = attachment
            fp.seek(0)
        if re.search("<</Key /Contents<", check_line.decode('UTF-8')):
            return False
        else:
            data = b''
            for i, line in enumerate(lines):
                if i != len(lines):
                    data = data + line
            with open(path_target, 'wb+') as fp:
                fp.write(data)
                return True
