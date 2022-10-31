from hashing import Hashing
from encryption import Encryption


class Verifying:
    @staticmethod
    def verify(path_file: str, path_key: str):
        Verifying.detach_pdf(path_file)
        original_filepath = path_file + "detach.pdf"
        digital_signature_filepath = path_file + "digital_signature.txt"
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
        # copy file asli ke file baru, ambil digital_signature lalu tulis ke key.txt,
        # file_baru = path_file + "detach.pdf"
        # file_key = path_file + "digital_signature.txt"
        # pdf tanpa digital_signature disimpan
        pass


# print(Verifying.verify(path_file="../testcase/test-paper.pdf", path_key="../testcase/test-private-key.pem"))
