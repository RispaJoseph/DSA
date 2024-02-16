class BST:
    def __init__(self,key):
        self.key=key
        self.lchild=None
        self.rchild=None

    def insert(self,data):
        if self.key is None:
            self.key=data
            return
        
        if self.key==data:
            return

        if data < self.key:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild=BST(data)
            
        else:
            if self.rchild:
                self.rchild.insert(data)
            
            else:
                self.rchild=BST(data)

    
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


root = BST(10)
list = [5,3,7,2,4,6,8]
for i in list:
  root.insert(i)
print()

inorder_traversal =root.inorder_traversal()
print(inorder_traversal)