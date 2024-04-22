import BST

t = BST()  

def contains(self, e):
    if self.Empty():
        return False
    if self.root == e:
        return True
    if e > self.root:
        return self.right.contains(e) and self.left.contains(e)
        
for e in range(10):
    if t.contains(e):
        print(e, ":yes")
    else:
        print(e, ":no")
