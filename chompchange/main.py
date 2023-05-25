import json
from glob import glob

from block import Block
from transaction import Transaction

def transmit(block: Block = ()):
    pass

def store(block: Block = ()):
    pass

def main():
    txns = []

    for file in glob("../mempool/*.json"):
        with open(file, "r") as fh:
            values = json.load(fh)
            txn = Transaction(**values)
        if txn:
            txns.append(txn)

    block = Block(txns)
    print(block)

if __name__ == "__main__":
    main()
