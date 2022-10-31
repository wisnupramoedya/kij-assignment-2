import fitz
import os

from hashing import Hashing
from encryption import Encryption


class Verifying:
    @staticmethod
    def verify(path_file: str, path_key: str):
        Verifying.detach_pdf(path_file)
        original_filepath = path_file.replace('_signed', '_unsigned')
        
        digital_signature_filepath = path_file[:12] + "digital_signature.txt"
        f = open(digital_signature_filepath, "br")
        digital_signature = f.read()
        
        signature_hash = Encryption.decrypt(data=bytes.fromhex(digital_signature.decode()), key_filepath=path_key)
        original_hash = Hashing.hash_sha256(original_filepath)
        if signature_hash == original_hash:
            return True
        else:
            return False

    @staticmethod
    def detach_pdf(path_file: str):
        doc = fitz.open(path_file)
        xref = doc.page_xref(2)
        #print(doc.xref_get_key(xref, 'Keys')[1])
        sign = doc.xref_get_key(xref, 'Keys')[1] 
        text_file = open('../testcase/digital_signature.txt', 'w')
        text_file.write(sign)
        text_file.close()

        original_filepath = path_file.replace('_signed', '_unsigned')
    
        doc.xref_set_key(xref, 'Keys', 'null')
        doc.save(original_filepath)
        # os.remove(path_file)

print(Verifying.verify(path_file="../testcase/test-paper_signed.pdf", path_key="../testcase/test-private-key.pem"))
