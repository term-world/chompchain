import json
import getpass
import pymerkle
from datetime import datetime

import os

# If the file exists, load it
if os.path.isfile("txns.json"):
    with open("txns.json", "r") as fh:
        txs = json.load(fh)
else:
    # If the file doesn't exist, it's blank
    txs = []

while True:
    tx = input("String to add: ")
    tx = {
        "data": tx,
        "user": getpass.getuser()
    }
    if tx == "q":
        break
    txs.append(tx)
    with open("txns.json", "w") as fh:
        json.dump(txs, fh)
