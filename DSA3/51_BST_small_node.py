class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def find_smallest_node(self):
    current = self
    while current.left:
        current = current.left
    return current

# Example usage:
# Constructing a sample binary search tree
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(7)
root.left.left = TreeNode(2)
root.left.right = TreeNode(6)

# Find the smallest node in the BST
smallest_node = find_smallest_node(root)
print("Smallest node in the BST:", smallest_node.key)  # Output: Smallest node in the BST: 2