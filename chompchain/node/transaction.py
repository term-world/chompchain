import json
import hashlib
from datetime import datetime
from ..wallet.wallet import Wallet

class Transaction:

    def __init__(self, **kwargs):
        for arg in kwargs:
            setattr(self, arg, kwargs[arg])

        if "hash" not in kwargs:
            hash = hashlib.new('sha256')
            hash.update(self.__str__().encode())
            setattr(self, "hash", hash.hexdigest())

        if "timestamp" not in kwargs:
            time = datetime.now().timestamp()
            setattr(self, "timestamp", time)

        if "signature" not in kwargs:
            wallet = Wallet()
            setattr(self,"signature",wallet.keys())
        

    def __str__(self):
        return json.dumps(self.__dict__, separators = (',', ':'))
