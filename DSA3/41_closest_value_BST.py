class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None    
        self.right = None

def closest_value(root, target):
    closest = root.val  
    min_diff = abs(root.val - target)  

    def inorder_traversal(node):
        nonlocal closest, min_diff
        if node:
            inorder_traversal(node.left)
            if abs(node.val - target) < min_diff:
                min_diff = abs(node.val - target)
                closest = node.val
            inorder_traversal(node.right)

    inorder_traversal(root)
    return closest


root = TreeNode(9)
root.left = TreeNode(4)
root.right = TreeNode(17)
root.left.left = TreeNode(3)
root.left.right = TreeNode(6)
root.left.right.left = TreeNode(5)
root.left.right.right = TreeNode(7)
root.right.right = TreeNode(22)
root.right.right.left = TreeNode(20)

target = 18
closest = closest_value(root, target)
print("Closest value to", target, "in the tree:", closest)
