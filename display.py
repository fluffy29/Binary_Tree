from display import BST

def display(self, level=0):
    if self.Empty():
        return
    self.left.display(level + 1)
    print(" " * 3 * level , self.root)
    self.right.display(level + 1)

    """
Adding elements to a BST
leaf addition: the near element will be a leaf of the 
resulting tree
    """
def add(self, e):
    if self.Empty():
      self.root = e
      self.left = BST()
      self.right = BST()
    if e == self.root:
        return self