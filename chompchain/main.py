import json
from glob import glob

from block import Block
from transaction import Transaction
from couchsurf import Connection

def transmit(block: Block = ()):
    pass

def store(block: Block = ()):
    conn = Connection("blocks")
    conn.request.put(
        doc_id = block.hash,
        doc = block.data,
        attachment = block.tree.pickle_data(),
        name = "tree.pkl"
    )

def main():
    txns = []

    for file in glob("../mempool/*.json"):
        with open(file, "r") as fh:
            values = json.load(fh)
            txn = Transaction(**values)
        if txn:
            txns.append(txn)

    block = Block(txns)
    store(block)

if __name__ == "__main__":
    main()
