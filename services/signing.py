from Crypto.PublicKey import RSA
from Crypto.Signature.pkcs1_15 import PKCS115_SigScheme
from Crypto.Hash import SHA256

from services.hashing import Hashing


class Signing:
    @staticmethod
    def sign(path_file: str, path_target: str, path_key: str) -> bool:
        f = open(path_file, "rb").read()
        hash = Hashing.hash_sha256(path_file)
        keyPair = RSA.import_key(open(path_key).read())
        signer = PKCS115_SigScheme(keyPair)
        signature = signer.sign(hash)
        with open(path_target, 'wb') as sign:
            with open(path_file, 'rb') as orig:
                sign.write(orig.read())
            sign.write(signature)
        return True

# Signing.sign("../testcase/test-1_3.pdf", "../testcase/test-1_3_signed.pdf", "../testcase/test-private-key.pem")