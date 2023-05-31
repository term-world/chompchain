import os
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5

class Wallet:

    def __init__(self):
        self.keys = {}
        self.wallet_dir = os.path.expanduser("~/.wallet")
        if not os.path.isdir(self.wallet_dir):
            os.mkdir(self.wallet_dir)
            self.__generate_keys()
            self.__set_permissions()
            self.__broadcast_keys()
        else: self.__open_keys()

    def __generate_keys(self):
        private_key = RSA.generate(4096)
        self.keys["cc_rsa"] = private_key
        self.keys["cc_rsa.pub"] = private_key.publickey()
        for key in self.keys:
            with open(f"{self.wallet_dir}/{key}", "wb") as fh:
                fh.write(self.keys[key].export_key())

    def __open_keys(self):
        keys = ["cc_rsa", "cc_rsa.pub"]
        for key in keys:
            with open(f"{self.wallet_dir}/{key}", "rb") as fh:
                self.keys[key] = fh.read()

    def __set_permissions(self):
        os.system(f"chmod 700 {self.wallet_dir}")
        for key in self.keys:
            os.system(f"chmod 600 {self.wallet_dir}/{key}")

    def __broadcast_keys(self):
        pass

    def sign(self, transaction: str = ""):
        signer = PKCS1_v1_5.new(RSA.import_key(self.keys["cc_rsa"]))
        signature = SHA256.new()
        signature.update(transaction.encode('utf-8'))
        return signer.sign(signature).hex()
