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

    def search(self,data):
        if self.key == data:
            print("Node Found")
            return
        if self.key > data:
            if self.lchild:
                self.lchild.search(data)
            else:
                print("Node not Found")
        
        if self.key < data:
            if self.rchild:
                self.rchild.search(data)
            else:
                print("Node not Found")


    def preorder(self):
        print(self.key)
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()

    def inorder(self):
        if self.lchild:
            self.lchild.inorder()
        print(self.key)
        if self.rchild:
            self.rchild.inorder()

    def postorder(self):
        if self.lchild:
            self.lchild.postorder()
        if self.rchild:
            self.rchild.postorder()
        print(self.key)


    def delete(self,data):
        if self.key is None:
            print("Tree is Empty")
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
    

    
def count(node):
    if node is None:
        return 0
    return 1 + count(node.lchild) + count(node.rchild)




root = BST(10)
list = [5,3,7,2,4,6,8]
for i in list:
  root.insert(i)
print()


print("Count : ")
print(count(root))
print()


root.search(5)
print()

# print("Pre-Order")
# root.preorder()
# print()

# print("Post-Order")
# root.postorder
# print()


# print("Inorder")
# root.inorder()



if count(root) >1:
    root.delete(3)
else:
    print("Can't perform deletion operation!")
print()


print("After Deleting : ")
root.preorder()


