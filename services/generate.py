from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from datetime import datetime
import random
import string

private_key_pass = b"kij-assignment"
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

now = datetime.now()
date_time = now.strftime("%Y-%m-%d-%H-%M-%S")
rand = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 5))

class Generate:
    def generate_private_key():
        encrypted_pem_private_key = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.BestAvailableEncryption(private_key_pass)
        )
        private_key_file = open(date_time + "_" + rand + "_privkey.pem", "w")
        private_key_file.write(encrypted_pem_private_key.decode())
        private_key_file.close()
        return "Done"

    def generate_public_key():
        pem_public_key = private_key.public_key().public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        public_key_file = open(date_time + "_" + rand + "_pubkey.pub", "w")
        public_key_file.write(pem_public_key.decode())
        public_key_file.close()
        return "Done"

Generate.generate_private_key()
Generate.generate_public_key()