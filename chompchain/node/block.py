import json
from datetime import datetime
from .tree import Tree
import getpass
from .chain import Chain
from .transaction import Transaction

class Block:

    def __init__(self, transactions: list = []):
        self.txns = transactions
        self.__create_block_tree()
        self.hash = self.__assign_hash().decode('utf-8')
        self.timestamp = datetime.now().timestamp() # DO NOT HASH
        self.data = {
            "user":getpass.getuser(),
            "cmd": "cd main" #TODO: import command inputted
        }

    def __assign_hash(self) -> str:
        """ Assigns block ID from Merkle tree """
        return self.tree.merkle.root

    def __create_block_tree(self) -> None:
        self.tree = Tree()
        for txn in self.txns:
            data = txn.__dict__.items()
            txn = {k:v for k,v in data if not k in ["hash", "timestamp"]}
            self.tree.append_data(json.dumps(txn, separators = (',', ':')))

    def __str__(self) -> str:
        return json.dumps({
            "hash": str(self.hash),
            "txns": [str(txn) for txn in self.txns],
            "prev_hash": self.prev_hash,
            "timestamp": self.timestamp
        }, separators = (',', ':'))
