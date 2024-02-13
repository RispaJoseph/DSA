# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = None
        self.right = None

    def validate(self):
        if self is None:
            return True
        while self.left:
            current=self.left
            if current.val<self.val:
                current=current.left
            else:
                return False
        while self.right:
            current=self.right
            if current.val>self.val:
                current=current.right
            else:
                return False
        

