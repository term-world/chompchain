import json
import hashlib
from datetime import datetime
from ..wallet.wallet import Wallet

class Transaction:

    def __init__(self, **kwargs):
        """ Constructor """
        # TODO: Every argument in kwargs _should_ be an entry in
        #       the self.data property

        # For every argument supplied as a keyword
        for arg in kwargs:
            # Set an object property for that keyword
            setattr(self, arg, kwargs[arg])

        # TODO: Determine if we just overwrite everything that
        #       comes in as a kwarg with the following values

        # If no hash in the kwargs
        if "hash" not in kwargs:
            hash = hashlib.new('sha256')
            hash.update(self.__str__().encode())
            setattr(self, "hash", hash.hexdigest())

        # If no timestamp in the kwargs
        if "timestamp" not in kwargs:
            time = datetime.now().timestamp()
            setattr(self, "timestamp", time)

        # If transaction is not signed
        if "signature" not in kwargs:
            # This loads or creates keys
            wallet = Wallet()
            # This affixes a signature to the transaction
            setattr(self,"signature",wallet.sign(str(self)))

    def __str__(self):
        return json.dumps(self.__dict__, separators = (',', ':'))
