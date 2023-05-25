import getpass
from tree import Tree

demo_tree = Tree()

while True:
    tx = input("String to add (hit `enter` to exit): ")
    tx = {
        "data": tx,
        "user": getpass.getuser()
    }
    if not tx["data"]: break
    demo_tree.append_data(tx)

demo_tree.pickle_data()

demo_tree.unpickle_data()

while True:
    data = input("Data entered: ")
    if not data: break
    user = input("User entered: ") or getpass.getuser()
    value = {
        "data": data,
        "user": user
    }
    demo_tree.is_included(value)
