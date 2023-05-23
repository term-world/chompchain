from pymerkle import MerkleTree, verify_inclusion, verify_consistency
import json

with open('demo_data.json', 'r') as f:
    serialized = json.load(f)

    tree = MerkleTree()
    proof = tree.prove_inclusion('bar')

    print(proof)
    deserialized = proof.deserialize(serialized)
    print(deserialized)
