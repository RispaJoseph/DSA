class TreeNode:
    def __init__(self,value):
        self.val = value
        self.left = None
        self.right = None

    def largest(self):
        current = self 

        while current.right and current.right.right:
            current = current.right
        if current.right:
            print(f"The second largest node {current.val}")
        else:
            print("The tree has less than 2 nodes")

root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(7)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.left = TreeNode(6)
root.right.right = TreeNode(8)


root.largest()

