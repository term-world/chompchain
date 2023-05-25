import json

from couchsurf import Connection

class Chain:

    """ Design of the chain has changed quite a bit """

    def __init__(self):
        self.conn = Connection("blocks")
        self.blocks = self.get_all_blocks()

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
