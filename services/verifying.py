from Crypto.PublicKey import RSA
from Crypto.Signature.pkcs1_15 import PKCS115_SigScheme
from Crypto.Hash import SHA256
import shutil

from services.hashing import Hashing
import random
import string
import os


class Verifying:
    @staticmethod
    def get_signature(file):
        with open(file, 'rb') as f:
            f.seek(-256, 2)
            return f.read()

    @staticmethod
    def verify(path_file: str, path_key: str) -> bool:
        rand = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        get_signature = Verifying.get_signature(path_file)
        signed_file = open(path_file, "rb").read()
        orig_file = signed_file[:-256]
        f = open(rand + ".pdf", "wb")
        f.write(orig_file)
        f.close()
        hash = Hashing.hash_sha256(rand + ".pdf")
        # hash = Hashing.hash_sha256(orig_file)
        os.remove(rand + ".pdf")
        keyPair = RSA.import_key(open(path_key).read())
        verifier = PKCS115_SigScheme(keyPair)
        try:
            verifier.verify(hash, get_signature)
            return True
        except:
            return False

# Verifying.verify("../testcase/test-1_3_signed.pdf", "../testcase/2022-11-07-12-39-30_J0A9A_pubkey.pub")