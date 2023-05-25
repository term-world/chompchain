import json
from datetime import datetime
from tree import Tree

class Block:

    def __init__(self, transactions: list = []):
        self.txns = transactions
        self.__create_block_tree()
        self.hash = self.__assign_hash()
        self.prev_hash = self.__retrieve_prev_hash()
        self.timestamp = datetime.now().timestamp() # DO NOT HASH

    def __assign_hash(self) -> str:
        """ Assigns block ID from Merkle tree """
        return self.tree.merkle.root

    def __retrieve_prev_hash(self) -> str:
        """ Retrieve hash from most previously hashed block """
        return "0"

    def __create_block_tree(self) -> None:
        self.tree = Tree()
        self.tree.append_data(self.txns)

    def __str__(self) -> str:
        return json.dumps({
            "hash": str(self.hash),
            "txns": [str(txn) for txn in self.txns],
            "prev_hash": self.prev_hash,
            "timestamp": self.timestamp
        })
