import json

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

    def __str__(self):
        return json.dumps(self.__dict__)
