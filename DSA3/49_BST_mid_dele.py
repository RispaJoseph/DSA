class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def find_middle_node(root):
    slow = root
    fast = root
    prev = None

    while fast and fast.right:
        prev = slow
        slow = slow.left
        fast = fast.right.right

    # If fast pointer reached the end (None), slow is at the middle node
    return slow, prev

def delete_node(root, key):
    if root is None:
        return root

    # Search for the node to delete
    if key < root.val:
        root.left = delete_node(root.left, key)
    elif key > root.val:
        root.right = delete_node(root.right, key)
    else:
        # Node to delete found

        # Case 1: Node has 0 or 1 child
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp

        # Case 2: Node has 2 children
        # Find the inorder successor (smallest node in right subtree)
        temp = root.right
        while temp.left:
            temp = temp.left

        # Copy the inorder successor's value to this node
        root.val = temp.val

        # Delete the inorder successor
        root.right = delete_node(root.right, temp.val)

    return root

# Example usage:
# Construct the BST
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(7)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.left = TreeNode(6)
root.right.right = TreeNode(8)

# Find the middle node and delete it
middle_node, prev = find_middle_node(root)
print("Middle node:", middle_node.val)
if prev:
    prev.left = delete_node(prev.left, middle_node.val)
else:
    root = delete_node(root, middle_node.val)

# Print the updated BST
# (Note: This is just for illustration, in a real application, you may traverse the BST to check the structure)
print("Updated BST:")
def inorder_traversal(root):
    if root is None:
        return
    inorder_traversal(root.left)
    print(root.val, end=" ")
    inorder_traversal(root.right)
inorder_traversal(root)

print(inorder_traversal)