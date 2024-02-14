class TreeNode:
    def __init__(self,value):
        self.val = value
        self.left = None
        self.right = None


def is_bst(root):
    def inorder_traversal(node):
        if node is None:
            return []
        return inorder_traversal(node.left)+[node.val]+inorder_traversal(node.right)
    
    inorder_sequence = inorder_traversal(root)

    for i in range(1,len(inorder_sequence)):
        if inorder_sequence[i] <= inorder_sequence[i-1]:
            return False
        return True

        



root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(7)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.left = TreeNode(6)
root.right.right = TreeNode(8)


print(is_bst(root))



