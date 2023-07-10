import pickle
from pymerkle import InmemoryTree as MerkleTree,verify_consistency,verify_inclusion

class Tree:

    def __init__(self):
        self.merkle = MerkleTree()
        self.pickled_tree = None

    def is_included(self,check: int) -> bool:
        size = self.merkle.get_size()
        try:
            proof = self.merkle.prove_inclusion(check,size)
            verify_inclusion(
                self.merkle.get_leaf(check),
                self.merkle.get_state(size),
                proof
            )
            return True
        except:
            return False

    def is_consistent(self,sublength: int,subroot: int) -> bool:
        try:
            proof = self.merkle.prove_consistency(sublength, subroot)
            verify_consistency(
                    self.merkle.get_state(sublength), 
                    self.merkle.get_state(subroot), 
                    proof
                )
            return True
        except:
            return False

    def pickle_data(self):
        self.pickled_tree = pickle.dumps(self.merkle)
        return self.pickled_tree

    def unpickle_data(self):
        return pickle.loads(self.pickled_tree)

    def append_data(self,data: any):
        if isinstance(data,bytes):
            self.merkle.append(data)
        else:
            for x in list(data):
                self.merkle.append(bytes(x,'utf-8'))
