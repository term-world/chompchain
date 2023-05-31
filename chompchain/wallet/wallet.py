import os
import json
import requests
from Crypto.PublicKey import RSA

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
        url = "https://dir.chain.chompe.rs/keys"  # the actual URL to send the keys
        
        payload = {
            "user": "username",  # Replace with the actual username
            "key": {
                    "public_key": self.keys["cc_rsa.pub"].export_key().decode()
            }
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                print("Keys successfully broadcasted.")
            else:
                print("Failed to broadcast keys. Status code:", response.status_code)
        except requests.exceptions.RequestException as e:
            print("Error occurred during key broadcasting:", e)

wallet = Wallet()