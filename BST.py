from BST import BinaryTree


class BST(BinaryTree):
    def contains(self, e):
        if self.Empty():
            return False
        if self.root == e:
            return True
        if e < self.root:
            return self.left.contains(e)
        else:
            return self.right.contains(e)

r = BST(8, BST(7), BST(), BST(1), BST())

for e in range(10):
            t = BinaryTree()
            if t.contains(e):
                print(e, ":yes")
            else:
                print(e, ":no")


   