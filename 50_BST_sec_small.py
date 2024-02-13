
class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def min_node(self):
        current = self
        while current.left and current.left.left:
            current = current.left
        if current.left:
            print(f'Second smallest value is {current.left.key}')
        else:
            print('Tree has less than 2 nodes')

# Example usage:
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(7)
root.left.right = TreeNode(2)
root.left.right = TreeNode(4)

# Call the min_node method to find the second smallest node
root.min_node()  # Output: Second smallest value is 3