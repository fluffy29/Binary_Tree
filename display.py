from display import BST


def display(self, level=0):
    if self.Empty():
        return
    self.left.display(level + 1)
    print(" " * 3 * level, self.root)
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

    for e in [5, 2, 8, 1, 4, 7]:
        t = BST()
        for e in [5, 2, 8, 1, 4, 7]:
            t = t.add(e)
            t.display()
            print()

    def root(a):
        for l in range(len(a)):
            for r in range(l + 1, len(a)):
                if a[l] > a[r]:
                    temp = a[1]
                a[l] = a[r]
                a[r] = temp

    def populate(t, b):
        if t.Empty():
            populate(t.left, b)
        b.append(t.root)
        populate(t.right, b)


t = BST()
for i in range(10):
    print(i, ":")
    t.lessThan(1).display()
