class TreeNode:
    def __init__(self,value):
        self.val = value
        self.left = None
        self.right = None
    
    def smallest(self):
        current = self

        while current.left:
            current = current.left
        return current.val
    
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(7)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)



small = root.smallest()
print(f"The smallest node in the tree is {small}")