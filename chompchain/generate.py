import json
import os
from glob import glob

from .block import Block
from .chain import Chain
from chompchainwallet import Transaction
from chompchainwallet import Wallet

def generate():
    txns = []
    wallet = Wallet()
    chain = Chain()

    # Harvest transactions
    files = glob("/mempool/*.json")
    for file in files:
        print(file)
        with open(file, "r") as fh:
            values = json.load(fh)
            txn = Transaction(
                wallet,
                **values
            ).to_dict()
        if txn:
            txns.append(txn)

    block = Block(txns)

    chain.add_block(block)

    # Erase files
    """
    for file in files:
        os.unlink(file)
    """
