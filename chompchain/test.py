from tree import Tree
import pickle

tree_block = Tree()
tree_block.append_data(["1","2","3","4"]) #create block
 
tree_chain = Tree() #create chain
tree_chain.append_data(pickle.dumps(tree_block)) #input byte of block to chain

tree_block_byte = tree_chain.merkle.leaves[0].entry #grab that block byte from the chain

tree_block_again = pickle.loads(tree_block_byte) #load that block byte

for x in range(tree_block_again.merkle.get_size()):
    byte = tree_block_again.merkle.leaves[x].entry
    print(str(byte,'utf-8')) #loads the appended block data

