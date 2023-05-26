import json
from glob import glob

from block import Block
from chain import Chain
from transaction import Transaction

def transmit(block: Block = ()):
    pass

def main():
    txns = []
    chain = Chain()
    for file in glob("../mempool/*.json"):
        with open(file, "r") as fh:
            values = json.load(fh)
            txn = Transaction(**values)
        if txn:
            txns.append(txn)
    block = Block(txns)
    chain.add_block(block)

if __name__ == "__main__":
    main()
