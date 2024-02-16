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
            print("Data is Found!")
            return
        if data < self.key:
            if self.lchild:
                self.lchild.search(data)
            else:
                print("Data not Found!")

        else:
            if self.rchild:
                self.rchild.search(data)
            else:
                print("Data not found!")

    def delete(self,data):
        if self.key is None:
            print("Tree is empty")
            return

        if data < self.key:
            if self.lchild:
                self.lchild = self.lchild.delete(data)
            else:
                print("Given node is not present in the tree!")
        elif data > self.key:
            if self.rchild:
                self.rchild = self.rchild.delete(data)
            else:
                print("Given node is not present in the tree!")
        else:
            if self.lchild is None:
                temp = self.rchild
                self = None
                return temp
            if self.rchild is None:
                temp = self.lchild
                self = None
                return temp
            
            node = self.rchild
            while node.lchild:
                node = node.lchild
            self.key = node.key
            self.rchild = self.rchild.delete(node.key)

        return self

                
    def count(self):
        if self is None:
            return 0
        return 1 + (self.lchild.count() if self.lchild else 0) + (self.rchild.count() if self.rchild else 0)
    



root = BST(15)
list = [20,16,22,14,17,21,23]
for i in list:
    root.insert(i)

print(root.inorder_traversal())
print()

root.search(4)
print()


print("Count of the nodes in the tree",root.count())
print()

c = root.count()

if c > 1:
    root.delete(15)
else:
    print("Can't perform deletion operation!")



print(root.inorder_traversal())
print()



    


