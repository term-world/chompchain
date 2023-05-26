from tree import Tree

cons_tree = Tree()#makes a new tree

cons_tree.append_data(["one","two","three"])#appends one,two,three

sublength = cons_tree.merkle.length
subroot = cons_tree.merkle.root
#takes the length and root of the tree at this point

cons_tree.append_data("four")#appends four to this tree

print(cons_tree.is_consistent(sublength,subroot))#proves that this tree is consistant with the old tree
print(subroot,cons_tree.merkle.root)

fake_tree = Tree()#creates a new tree

print(fake_tree.is_consistent(sublength,subroot))#fails as this tree is not conistanct with the root we had

fake_tree.append_data(["one","two","three"])#adds the same data as the given point before

print(fake_tree.is_consistent(sublength,subroot))#passes because the data is the same??
print(subroot,fake_tree.merkle.root)