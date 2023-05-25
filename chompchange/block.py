import json
from datetime import datetime

class Block:

    def __init__(self, transactions: list = []):
        self.txns = transactions
        self.tree = None # Merkle tree representation
        self.hash = self.__assign_hash() # Assign root hash of tree
        self.prev_hash = self.__retrieve_prev_hash()
        self.timestamp = datetime.now().timestamp() # DO NOT HASH

    def __assign_hash(self) -> str:
        """ Assigns block ID from Merkle tree """
        pass

    def __retrieve_prev_hash(self) -> str:
        """ Retrieve hash from most previously hashed block """
        return "0"

    def __str__(self) -> str:
        return json.dumps({
            "hash": self.hash,
            "txns": [str(txn) for txn in self.txns],
            "prev_hash": self.prev_hash,
            "timestamp": self.timestamp
        })
