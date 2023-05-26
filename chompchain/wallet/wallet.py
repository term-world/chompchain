import os
from Crypto.PublicKey import RSA

class Wallet:

    def __init__(self):
        self.keys = {}
        self.wallet_dir = os.path.expanduser("~/.wallet")
        if not os.path.isdir(self.wallet_dir):
            self.__generate_keys()
            self.__set_permissions()
            self.__broadcast_keys()
        else: self.__open_keys()

    def __generate_keys(self):
        private_key = RSA.generate(4096)
        self.keys["cc_rsa"] = private_key.export_key(
            pkcs = 8,
            protection = "scryptAndAES128-CBC"
        )
        self.keys["cc_rsa.pub"] = private_key.publickey().export_key()
        for key in self.keys:
            with open(f"{self.wallet_dir}/{key}", "wb") as fh:
                fh.write(self.keys[key])

    def __open_keys(self):
        keys = ["cc_rsa", "cc_rsa.pub"]
        for key in keys:
            with open(f"{self.wallet_dir}/{key}", "rb") as fh:
                self.keys[key] = fh.read()

    def __set_permissions(self):
        os.system(f"chmod 600 {self.wallet_dir} -R")

    def __broadcast_keys(self):
        pass
