import pickle
from pymerkle import MerkleTree, verify_inclusion, verify_consistency

class Tree:

    def __init__(self):
        self.merkle = MerkleTree()
        self.pickled_tree = None

    def is_included(self,check) -> bool:
        check = str(check)
        try:
            proof = self.merkle.prove_inclusion(check)
            verify_inclusion(check,self.merkle.root,proof)
            return True
        except:
            return False

    def is_consistent(self,sublength,subroot) -> bool:
        try:
            proof = self.merkle.prove_consistency(sublength, subroot)
            verify_consistency(subroot, self.merkle.root, proof)
            return True
        except:
            print("invalid tree!")
            return False

    def pickle_data(self):
        self.pickled_tree = pickle.dumps(self.merkle)
        return self.pickled_tree

    def unpickle_data(self):
        return pickle.loads(self.pickled_tree)

    def append_data(self,data):
        if type(data) == list:
            for x in data: self.merkle.append_entry(str(x))
        else:
            self.merkle.append_entry(str(data))
