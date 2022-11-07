from Crypto.PublicKey import RSA
from Crypto.Signature.pkcs1_15 import PKCS115_SigScheme
from Crypto.Hash import SHA256
import shutil


class Verifying:
    @staticmethod
    def get_signature(file):
        with open(file, 'rb') as f:
            f.seek(-256, 2)
            return f.read()

    @staticmethod
    def verify(path_file: str, path_key: str) -> bool:
        get_signature = Verifying.get_signature(path_file)
        signed_file = open(path_file, "rb").read()
        orig_file = signed_file[:-256]
        hash = SHA256.new(orig_file)
        keyPair = RSA.import_key(open(path_key).read())
        verifier = PKCS115_SigScheme(keyPair)
        try:
            verifier.verify(hash, get_signature)
            print("true")
            return True
        except:
            print("false")
            return False

Verifying.verify("../testcase/test-1_3_signed.pdf", "../testcase/2022-11-07-12-39-30_J0A9A_pubkey.pub")