class TreeNode:
    def __init__(self,value):
        self.val = value
        self.left = None
        self.right = None

def min_depth(root):
    if root is None:
        return 0
    if not root.left:
        return 1 + min_depth(root.right)
    if not root.right:
        return 1 + min_depth(root.left)
    if not root.left and not root.right:
        return 1
    return 1 + min(min_depth(root.left),min_depth(root.right))    

# root = TreeNode(3)
# root.left = TreeNode(9)
# root.right = TreeNode(20)
# root.right.left = TreeNode(15)
# root.right.right = TreeNode(7)


root = TreeNode(2)
root.right = TreeNode(3)
root.right.right = TreeNode(4)
root.right.right.right = TreeNode(5)
root.right.right.right.right = TreeNode(6)

print(min_depth(root))