import json
import hashlib
from datetime import datetime

class Transaction:

    def __init__(self, **kwargs):
        for arg in kwargs:
            setattr(self, arg, kwargs[arg])

        # Transactions which are not coin exchange should
        # "sign themselves" in order to guarantee integrity

        # The plan here would be for each node to have a private
        # hash or key generated on startup which would then sign
        # transactions and somehow transmit its public key with
        # the block to network for verification

        if "hash" not in kwargs:
            hash = hashlib.new('sha256')
            hash.update(self.__str__().encode())
            setattr(self, "hash", hash.hexdigest())

        if "timestamp" not in kwargs:
            time = datetime.now().timestamp()
            setattr(self, "timestamp", time)

    def __str__(self):
        return json.dumps(self.__dict__)
