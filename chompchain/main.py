import json
import os
from glob import glob

from .block import Block
from .chain import Chain
from chompchainwallet import Transaction
from chompchainwallet import Wallet

def main():
    txns = []
    wallet = Wallet()
    chain = Chain()
    # Harvest transactions
    files = glob("/mempool/*.json")
    for file in files:
        print(file)
        with open(file, "r") as fh:
            values = json.load(fh)
            txn = Transaction(to_addr = "100x4d967e796ca2bc965c6026fc79196f3cf94804f1afdc5fc41c8b7492cfedac81",**values).to_dict()
        if txn:
            txns.append(txn)

    block = Block(txns)

    chain.add_block(block)
    # Erase files
    """
    for file in files:
        os.unlink(file)
    """

if __name__ == "__main__":
    main()
