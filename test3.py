class TreeNode:
    def __init__(self,value):
        self.val = value
        self.left = None
        self.right = None

def closest_value(root,target):
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





        
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(7)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.left = TreeNode(6)
root.right.right = TreeNode(8)

target = 1
result = closest_value(root,target)

print("The closest value is ",result)