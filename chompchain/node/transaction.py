import json
import hashlib
from datetime import datetime
from ..wallet.wallet import Wallet

class Transaction:

    def __init__(self, **kwargs):
        """ Constructor """
        self.data = {}

        for arg in kwargs:
            self.data[arg] = kwargs[arg]

        hash = hashlib.new('sha256')
        hash.update(self.__str__().encode())
        setattr(self, "hash", hash.hexdigest())

        time = datetime.now().timestamp()
        setattr(self, "timestamp", time)

        wallet = Wallet()
        setattr(self,"signature",wallet.sign(str(self)))

    def give_json(self):
        return self.__dict__

    def __str__(self):
        return json.dumps(self.__dict__, separators = (',', ':'))
