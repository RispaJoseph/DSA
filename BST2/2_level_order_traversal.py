class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def levelorder(root):
    result = []
    

root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(7)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.left = TreeNode(6)
root.right.right = TreeNode(8)