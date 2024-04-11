class BinaryTree:
    def __init__(self, r=None, L=None, R=None):
        self.root = r
        self.left = L
        self.right = R

    def depthfirst(self):
        if self.root is not None:
            print(self.root)
        if self.left is not None:
            self.left.depthfirst()
        if self.right is not None:
            self.right.depthfirst()

    def contains(self, e):
        if self.Empty():
            return False
        if self.root == e:
            return True
        if self.left.contains(e) or self.right.contains(e):
            return True

    def height(self):
        if self.Empty():
            return -1
        return 1 + max(self.left.height(), self.right.height())

    def pathlength(self):
        if self.Empty():
            return 0
        return 1 + self.left.pathlength() + self.right.pathlength()
