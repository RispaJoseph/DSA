class TreeNode:
    def __init__(self,value):
        self.val = value
        self.left = None
        self.right = None

def InorderTraversal(root):
    res = []
    
    if root is None:
        return []
    A = InorderTraversal(root.left)
    res.extend(A)
    res.append(root.val)
    B = InorderTraversal(root.right)
    res.extend(B)

    return res


def PreorderTraversal(root):
    res = []
    
    if root is None:
        return []
    res.append(root.val)
    A = PreorderTraversal(root.left)
    res.extend(A)
    B = PreorderTraversal(root.right)
    res.extend(B)

    return res


def PostorderTraversal(root):
    res = []

    if root is None:
        return []
    A = PostorderTraversal(root.left)
    res.extend(A)
    B = PostorderTraversal(root.right)
    res.extend(B)
    res.append(root.val)

    return res
        

root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(7)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.left = TreeNode(6)
root.right.right = TreeNode(8)

print("Inorder Traversal = ",InorderTraversal(root))
print("Preorder Traversal = ",PreorderTraversal(root))
print("Postorder Traversal = ",PostorderTraversal(root))


# Inorder Traversal: [2, 3, 4, 5, 6, 7, 8]
# Preorder Traversal: [5, 3, 2, 4, 7, 6, 8]
# Postorder Traversal: [2, 4, 3, 6, 8, 7, 5]

