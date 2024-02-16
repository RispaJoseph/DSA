class TreeNode:
    def __init__(self,value):
        self.val = value
        self.left = None
        self.right = None

def inorder_traversal(root):
    res = []
    if root is None:
        return []
    A = inorder_traversal(root.left)
    res.extend(A)
    res.append(root.val)
    B = inorder_traversal(root.right)
    res.extend(B)
    return res


root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(7)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.left = TreeNode(6)
root.right.right = TreeNode(8)

print(inorder_traversal(root))
