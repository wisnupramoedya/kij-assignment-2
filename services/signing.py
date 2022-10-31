import codecs
import fitz
import os

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
    def sign(path_file: str, path_key: str):
        Signing.attach_pdf(path_file, Signing.get_digital_signature(path_file=path_file, path_key=path_key))

    @staticmethod
    def attach_pdf(path_file: str, digital_signature: str):
        doc = fitz.open(path_file)
        xref = doc.page_xref(2)
        doc.xref_set_key(xref, 'Keys', '(' + digital_signature + ')')
        doc.save(os.path.splitext(path_file)[0] + '_signed.pdf')
        # os.remove(path_file)


# sign = Signing.get_digital_signature("../testcase/test-paper.pdf", "../testcase/test-public-key.pub")
# print(sign)
