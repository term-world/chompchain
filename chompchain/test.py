from tree import Tree

tree1 = Tree().merkle

tree1.append(b"1")
tree1.append(b"2")
tree1.append(b"3")

tree2 = Tree().merkle

tree2.append(b"4")
tree2.append(b"5")
tree2.append(b"6")

tree3 = Tree().merkle

tree3.append(b"tree1")
tree3.append(b"tree2")

print(tree3)