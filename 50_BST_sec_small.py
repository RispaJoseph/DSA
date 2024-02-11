
class TreeNode:
    def __init__(self, key):
        self.key = key
        self.lchild = None
        self.rchild = None

    def min_node(self):
        current = self
        while current.lchild and current.lchild.lchild:
            current = current.lchild
        if current.lchild:
            print(f'Second smallest value is {current.lchild.key}')
        else:
            print('Tree has less than 2 nodes')

# Example usage:
root = TreeNode(5)
root.lchild = TreeNode(3)
root.rchild = TreeNode(7)
root.lchild.lchild = TreeNode(2)
root.lchild.rchild = TreeNode(4)

# Call the min_node method to find the second smallest node
root.min_node()  # Output: Second smallest value is 3