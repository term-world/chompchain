from pymerkle import MerkleTree, verify_inclusion, verify_consistency
import pickle

class Tree:

    def __init__(self):
        self.tree = MerkleTree()
        self.pickled_tree = None

    def is_included(self,check):
        check = str(check)
        try:
            proof = self.tree.prove_inclusion(check)
            verify_inclusion(check,self.tree.root,proof)
            print("verified")
            return proof
        except:
            print("invalid entry")
            return

    def is_consistant(self,sublength,subroot):
        try:
            proof = tree.prove_consistency(sublength, subroot)
            verify_consistency(subroot, self.tree.root, proof)
            print("verified")
            return proof
        except:
            print("invalid entry")
            return

    def pickle_data(self):
        self.pickled_tree = pickle.dumps(self.tree)
        return self.pickled_tree

    def unpickle_data(self):
        return pickle.loads(self.pickled_tree)

    def append_data(self,data):
        if type(data) == list:
            for x in data: self.tree.append_entry(str(x))
        else:
            self.tree.append_entry(str(data))
        
        