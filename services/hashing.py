from Crypto.Hash import SHA256

class Hashing:
    @staticmethod
    def hash_sha256(path_file: str):
        f = open(path_file, "br")
        sha = SHA256.new()
        return sha

# print(Hashing.hash_sha256("../testcase/test-1_3.pdf"))