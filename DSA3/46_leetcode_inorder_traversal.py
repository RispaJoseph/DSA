# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import List

class Solution:
    def preorderTraversal(self, root):
        res = []

        def preorder(root):
            if not root:
                return
            res.append(root.val) 
            preorder(root.left)
            preorder(root.right)
            
        preorder(root)
        return res


root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)


solution = Solution()
preorder_result = solution.preorderTraversal(root)


print("Preorder traversal:", preorder_result)
