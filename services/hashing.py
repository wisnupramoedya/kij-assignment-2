from Crypto.Hash import SHA256


class Hashing:
    @staticmethod
    def hash_sha256(path_file: str) -> bytes:
        f = open(path_file, "br")
        sha = SHA256.new()
        while True:
            data = f.read(1024)
            if not data:
                break
            sha.update(data)
        f.close()
        return sha.hexdigest().encode()


filepath = "../testcase/test-paper.pdf"

print(Hashing.hash_sha256(filepath))
