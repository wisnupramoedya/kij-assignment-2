import fitz
import os

from hashing import Hashing
from encryption import Encryption

class Verifying:
    @staticmethod
    def verify(path_file: str, path_key: str):
        Verifying.detach_pdf(path_file)
        f = open("testcase/digital_signature.txt", "br")
        digital_signature = f.read()
        print(digital_signature.decode())

        signature_hash = Encryption.decrypt(data=bytes.fromhex(digital_signature.decode()), key_filepath=path_key)
        original_hash = Hashing.hash_sha256(path_file[:-7])
        print(original_hash)
        print(signature_hash)
        if signature_hash == original_hash:
            return True
        else:
            return False

    @staticmethod
    def detach_pdf(path_file: str):
        doc = fitz.open(path_file)
        xref = doc.page_xref(0)
        #print(doc.xref_get_key(xref, 'Keys')[1])
        sign = doc.xref_get_key(xref, 'Keys')[1]
        text_file = open('testcase/digital_signature.txt', 'w')
        text_file.write(sign)
        text_file.close()
    
        # doc.xref_set_key(xref, 'Keys', 'null')
        # doc.save(original_filepath + '.orig')
        # os.remove(path_file)

print(Verifying.verify(path_file="testcase/test-1_4_copy.pdf.hashed", path_key="testcase/test-private-key.pem"))
