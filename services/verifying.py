from services.hashing import Hashing
from services.encryption import Encryption


class Verifying:
    def verify(self, path_file: str, path_key: str):
        self.detach_pdf(path_file)
        f = open(self.digital_signature_filepath, "br")
        digital_signature = f.read()
        signature_hash = Encryption.decrypt(data=digital_signature, key_filepath=path_key)
        original_hash = Hashing.hash_sha256(self.original_filepath)
        if signature_hash == original_hash:
            return True
        else:
            return False

    def detach_pdf(self, path_file: str):
        # copy file asli ke file baru, ambil digital_signature lalu tulis ke key.txt,
        # pdf tanpa digital_signature disimpan
        # assign self.original_filepath
        # assign self.digital_signature_filepath
        pass
