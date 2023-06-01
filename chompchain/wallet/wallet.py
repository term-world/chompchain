import os
import json
import requests
from Crypto.Hash import SHA256
from Crypto.Hash import keccak
from Crypto.PublicKey import ECC
from Crypto.Signature import DSS

class Wallet:

    def __init__(self):
        self.keys = {}
        self.wallet_dir = os.path.expanduser("~/.wallet")
        if not os.path.isdir(self.wallet_dir):
            os.mkdir(self.wallet_dir)
            self.__generate_keys()
            self.__set_permissions()
            self.__derive_address()
            self.__broadcast_keys()

    def __generate_keys(self) -> None:
        private_key = ECC.generate(curve = 'P-256')
        self.keys[".cc.priv"] = private_key
        self.keys[".cc.pub"] = private_key.public_key()
        for key in self.keys:
            with open(f"{self.wallet_dir}/{key}", "wt") as fh:
                fh.write(self.keys[key].export_key(format = "PEM"))

    def __set_permissions(self) -> None:
        os.system(f"chmod 700 {self.wallet_dir}")
        for key in self.keys:
            os.system(f"chmod 600 {self.wallet_dir}/{key}")

    def __derive_address(self) -> None:
        pub_key = self.keys[".cc.pub"].export_key(format = 'raw')
        addr_hash = keccak.new(digest_bits=256)
        addr_hash.update(pub_key)
        self.address = f"0x{addr_hash.hexdigest()[-40:]}"

    def __broadcast_keys(self) -> bool:
        url = "https://dir.chain.chompe.rs/keys"  # the actual URL to send the keys
        payload = {
            "user": "username",  # Replace with the actual username
            "key": {
                "public_key": str(self.keys[".cc.pub"])
            }
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                return True
            raise
        except requests.exceptions.RequestException as e:
            return False

    def sign(self, transaction: str = ""):
        key = ECC.import_key(open(f"{self.wallet_dir}/.cc.priv").read())
        hashed_tx = SHA256.new(transaction.encode('utf-8'))
        signer = DSS.new(key, 'fips-186-3')
        return signer.sign(hashed_tx).hex()