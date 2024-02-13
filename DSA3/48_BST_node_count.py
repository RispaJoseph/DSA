class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def is_bst(root):
    def inorder_traversal(node):
        if node is None:
            return []
        return inorder_traversal(node.left) + [node.val] + inorder_traversal(node.right)
    
    return inorder_traversal(root)

# Example usage:
# Constructing a sample binary tree
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(7)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.left = TreeNode(6)
root.right.right = TreeNode(8)

# Get the list obtained from inorder traversal
inorder_list = is_bst(root)
print(inorder_list)
print(len(inorder_list))
