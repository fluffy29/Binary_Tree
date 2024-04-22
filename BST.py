def contains(self, e):
        if self.Empty():
            return False
        if self.root == e:
            return True
        if e > self.root:
            return self.right.contains(e) and self.left.contains(e)
        return self.left.contains(e) if e < self.root else self.right.contains(e)