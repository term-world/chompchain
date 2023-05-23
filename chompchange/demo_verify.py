import json
import pymerkle
import random
import pickle

with open("txns.json", "r") as fh:
    data = json.load(fh)

random.shuffle(data)

tree = pymerkle.MerkleTree()

for entry in data:
    tree.append_entry(json.dumps(entry))

while True:
    data = input("Data entered: ")
    user = input("User entered: ")
    value = {
        "data": data,
        "user": user
    }
    try:
        proof = tree.prove_inclusion(json.dumps(value))
        print("proved")
    except:
        print("NOT THERE!")
        break

with open("block.pkl", "wb") as fh:
    pickle.dump(tree, fh)
