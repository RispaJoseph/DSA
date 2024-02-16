class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def insert(root,data):
    if root is None:
        return TreeNode(data)
    
    if data < root.data:
        root.left = insert(root.left,data)
    
    elif data > root.data:
        root.right = insert(root.right,data)

    else:
        pass

    return root 



root = None

root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(7)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.left = TreeNode(6)
root.right.right = TreeNode(8)

# print(root,)

a= insert(root,100)
print(a.data)







