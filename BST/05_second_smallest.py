class TreeNode:
    def __init__(self,value):
        self.val = value
        self.left = None
        self.right = None
    
    def second_smallest(self):
        current = self

        while current.left and current.left.left:
            current = current.left
        if current.left:
            print(f'The 2nd smallest value in the tree is {current.left.val}')
        else:
            print("Tree has less than 2 nodes")


root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(7)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)



root.second_smallest()