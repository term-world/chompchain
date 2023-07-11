import json
from datetime import datetime
from .tree import Tree
from .chain import Chain
from chompchainwallet import Transaction

class Block:

    def __init__(self, transactions: list = []):
        self.txns = transactions
        self.__create_block_tree()
        self.hash = self.__assign_hash()
        self.timestamp = datetime.now().timestamp() # DO NOT HASH
        self.data = {
            "txns": [str(txn) for txn in transactions],
            "timestamp": self.timestamp
        }

    def __assign_hash(self) -> str:
        """ Assigns block ID from Merkle tree """
        return self.tree.merkle.root.value.hex()

    def __create_block_tree(self) -> None:
        self.tree = Tree()
        for txn in self.txns:
            data = txn.items()
            txn = {k:v for k,v in data if not k in ["hash", "timestamp", "signature"]}
            self.tree.append_data(txn['data'])

    def __str__(self) -> str:
        return json.dumps({
            "hash": str(self.hash),
            "txns": [str(txn) for txn in self.txns],
            "prev_hash": self.prev_hash,
            "timestamp": self.timestamp
        }, separators = (',', ':'))
