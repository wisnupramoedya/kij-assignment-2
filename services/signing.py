import codecs
import fitz
import os
import pickle

from hashing import Hashing
from encryption import Encryption

class Signing:
    @staticmethod
    def get_digital_signature(path_file: str, path_key: str) -> str:
        hashed_data = Hashing.hash_sha256(path_file=path_file)
        digital_signature = Encryption.encrypt(data=hashed_data, key_filepath=path_key)
        hex_ds = codecs.encode(digital_signature, 'hex')
        str_ds = hex_ds.decode()
        return str_ds

    @staticmethod
    def sign(path_file: str,  path_target: str, path_key: str):
        Signing.attach_pdf(path_file, path_target, Signing.get_digital_signature(path_file=path_file, path_key=path_key))

    @staticmethod
    def attach_pdf(filepath: str, path_target: str, digital_signature: str):
        attachment = bytes(f'<</Key /Contents<{digital_signature}>>>\r\n', 'UTF-8')
        print(attachment)
        position = 0
        eof = b''
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
            print(len(lines))
            print(position)
            lines.append(lines[position-1])
            print(lines[position])
            lines[position-1] = attachment
            fp.seek(0)
            print()
            print(len(lines))
            print(position)
            # fp.truncate(0)
        data = b''
        for i, line in enumerate(lines):
            if i != len(lines):
                data = data + line
        with open(path_target, 'wb+') as fp:
            fp.write(data)

# sign = Signing.get_digital_signature("../testcase/test-paper.pdf", "../testcase/test-public-key.pub")
# print(sign)
Signing.sign("testcase/test-1_3.pdf", "testcase/test-1_3_hashed.pdf","testcase/test-public-key.pub")

# Signing.sign(path_file="testcase/test-1_4_copy.pdf", path_key="testcase/test-public-key.pub")