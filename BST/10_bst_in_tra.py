class BST:
    def __init__(self,key):
        self.key = key
        self.lchild = None
        self.rchild = None
    
    def insert(self,data):
        if self.key is None:
            self.key = data
            return 
        if self.key == data:
            return
        if data < self.key:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = BST(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = BST(data)

    def inorder_traversal(self):
        res = []
        if self is None:
            return []
        if self.lchild:
            res.extend(self.lchild.inorder_traversal())
        res.append(self.key)
        if self.rchild:
            res.extend(self.rchild.inorder_traversal())
        
        return res
    

    def preorder_traversal(self):
        res = []

        if self is None:
            return []
        res.append(self.key)
        if self.lchild:
            res.extend(self.lchild.preorder_traversal())
        if self.rchild:
            res.extend(self.rchild.preorder_traversal())

        return res
    

    def postorder_traversal(self):
        res = []
        if self is None:
            return []
        if self.lchild:
            res.extend(self.lchild.postorder_traversal())
        if self.rchild:
            res.extend(self.rchild.postorder_traversal())
        res.append(self.key)

        return res
            

    

root = BST(5)
list = [3,7,2,4,6,8]
for i in list:
    root.insert(i)
print()

print("Inorder Traversal")
print(root.inorder_traversal())
print()


print("Preorder Traversal")
print(root.preorder_traversal())
print()

print("Postorder Traversal")
print(root.postorder_traversal())
print()
