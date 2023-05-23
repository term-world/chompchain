from pymerkle import MerkleTree, verify_inclusion, verify_consistency
import json

tree = MerkleTree()

# Populate tree with some entries
for data in ['foo', 'bar', 'baz', 'qux', 'quux']:
    tree.append_entry(data)

# Prove and verify inclusion of `bar`
proof = tree.prove_inclusion('bar')
verify_inclusion('bar', tree.root, proof)

#I think we would have it so the program always used `prove_consistancy` instead of `prove_inclusion`
#This way we would be proving the trees are consistant with one another
#This line creates a serialized version of the proof and store it in a theoretical json that would be couchdb
#we would need to create another file or way to store the tree itself
serialized = proof.serialize()
with open('demo_data.json', 'w') as f:
  json.dump(serialized,f,indent = 2)

# Save current state
sublength = tree.length
subheight = tree.height
subsize = tree.size
subroot = tree.root

# Append further entries
for data in ['corge', 'grault', 'garlpy']:
    tree.append_entry(data)

# Prove and verify previous state before these entries were made in order to verify consistancy
proof = tree.prove_consistency(sublength, subroot)
verify_consistency(subroot, tree.root, proof)

# Print out the root and all leaves of the tree 
print("Root of Tree:\n",tree.root, "\nLeaves of the Tree:")
for x in range(tree.length):
    print(tree.leaf(x))

deserialized = proof.deserialize(serialized)
print(deserialized)
