from datetime import datetime
import random
import string
from Crypto.PublicKey import RSA


key = RSA.generate(2048)

now = datetime.now()
date_time = now.strftime("%Y-%m-%d-%H-%M-%S")
rand = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))


class Generate:
    @staticmethod
    def generate_private_key():
        filepath = "testcase/" + date_time + "_" + rand + "_privkey.pem"
        private_key_file = open(filepath, "bw")
        private_key_file.write(key.exportKey("PEM"))
        private_key_file.close()
        return filepath

    @staticmethod
    def generate_public_key():
        filepath = "testcase/" + date_time + "_" + rand + "_pubkey.pub"
        public_key_file = open(filepath, "wb")
        public_key_file.write(key.public_key().exportKey("PEM"))
        public_key_file.close()
        return filepath


# Generate.generate_private_key()
# Generate.generate_public_key()