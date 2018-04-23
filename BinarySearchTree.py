class BinTree:
    
    def __init__(self, value):
        self.value = value
        self.left_tree = None
        self.right_tree = None

    def set_value(self, value):
        self.value = value

    def get_right_tree(self):
        return self.right_tree

    def get_left_tree(self):
        return self.left_tree

    def set_left_tree(self, left_tree):
        self.left_tree = left_tree

    def set_right_tree(self, right_tree):
        self.right_tree = right_tree

    def print_tree(self):
        sus = "("
        if(self.left_tree is not None):
            sus = sus + "" + self.left_tree.print_tree()
        sus = sus + "" + self.value

        if(self.right_tree is not None):
            sus = sus + "" + self.right_tree.print_tree()

        sus = sus + ")"

        return sus

root = BinTree("A")

print(root.print_tree())
leaf = [root]
for i in range(66, 91):
    temp = leaf.pop(0)
    right = BinTree(str(chr(i+1)))
    left = BinTree(str(chr(i)))
    temp.set_right_tree(right)
    temp.set_left_tree(left)
    leaf.append(left)
    leaf.append(right)

print(root.print_tree())

