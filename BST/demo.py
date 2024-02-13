class TreeNode:
    def __init__(self,value):
        self.val = value
        self.left = None
        self.right = None

class solution:
    def preorderTraversal(self,root):
        res = []

        if not root:
            return []
        res.append(root.val)
        a = self.preorderTraversal(root.left)
        res.extend(a)
        b = self.preorderTraversal(root.right)
        res.extend(b)

        return res
    

root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(7)
root.left.left = TreeNode(2) 
root.left.right = TreeNode(4)
root.right.left = TreeNode(6)
root.right.right = TreeNode(8)

s = solution()
print(s.preorderTraversal(root))
