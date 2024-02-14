class TreeNode:
    def __init__(self,value):
        self.val = value
        self.left = None
        self.right = None


    def largest(self):
        current = self

        while current.right:
            current = current.right
        return current.val

root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(7)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.left = TreeNode(6)
root.right.right = TreeNode(8)

largest = root.largest()
print(f"The largest number in the tree is {largest}")