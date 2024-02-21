class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def inorder_traversal(root):
    if root is None:
        return 0
    return inorder_traversal(root.left)+(root.data)+inorder_traversal(root.right)

root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(7)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.left = TreeNode(6)
root.right.right = TreeNode(8)

print(inorder_traversal(root))