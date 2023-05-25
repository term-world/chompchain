import json
import pickle

from tree import Tree

from couchsurf import Connection

class Chain:

    """ Design of the chain has changed quite a bit """

    def __init__(self):
        self.conn = Connection("blocks")
        self.blocks = self.get_all_blocks()
        self.tree = self.__construct_tree()

    def __construct_tree(self):
        block_tree = Tree()
        for block in self.blocks:
            block_tree.append_data(block["txns"])
        return block_tree

    def __retrieve_single_block(self, id: str = ""):
        if id:
            block = filter(lambda blk: blk["_id"] != id, self.blocks)
            return list(block)[0]
        return None

    def add_block(self, block):
        hashes = [block["_id"] for block in self.blocks]
        # Prevent duplicate blocks for testing
        if block.hash not in hashes:
            block.data["prev_hash"] = self.latest_block()["_id"]
            self.conn.request.put(
                doc_id = block.hash,
                doc = block.data,
                attachment = block.tree.pickle_data(),
                name = "tree.pkl"
            )

    def prove_block(self, id: str = "") -> bool:
        block = self.__retrieve_single_block(id)
        if block:
            tree = Tree()
            raw = self.conn.request.download(
                f"{block['_id']}/tree.pkl"
            )
            tree.merkle = pickle.loads(raw)
            try:
                tree.is_consistent(tree.merkle.length, tree.merkle.root)
                return True
            except:
                return False
        return False

    def get_all_blocks(self) -> list:
        blocks = self.conn.request.query(
            _id = {"op": "GREATER THAN", "arg": ""}
        )
        return sorted(
            blocks["docs"],
            key = lambda block: block["timestamp"],
            reverse = True
        )

    def latest_block(self):
        if len(self.blocks) > 0:
            return self.blocks[0]
        return 0
