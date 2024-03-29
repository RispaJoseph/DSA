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
    

    def search(self,data):
        if self.key == data:
            print("Data Found")
            return
        
        if data < self.key:
            if self.lchild:
                self.lchild.search(data)
            else:
                print("Data not found!")
        else:
            if self.rchild:
                self.rchild.search(data)
            else:
                print("Data not found!")


    def count(self):
        if self is None:
            return 0
        return 1 + (self.lchild.count() if self.lchild else 0) + (self.rchild.count() if self.rchild else 0)

    

    
root = BST(5)
list = [3,7,2,4,6,8]
for i in list:
    root.insert(i)
print()

print("Inorder Traversal ",root.inorder_traversal())
print()

root.search(71)
print()

print("Count of the total number of nodes : ",root.count())