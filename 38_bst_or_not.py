class TreeNode:
    def __init__(self,value):
        self.val = value
        self.left = None
        self.right = None


def is_bst(root):
    def inorder_traversal(node):
        if node is None:
            return []
        return inorder_traversal(node.left) + [node.val] + inorder_traversal(node.right)
    
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

print("Is the tree BST : ",is_bst(root))






# class TreeNode:
#     def __init__(self, key):
#         self.key = key
#         self.lchild = None
#         self.rchild = None

#     def min_node(self):
#         current = self
#         while current.lchild and current.lchild.lchild:
#             current = current.lchild
#         if current.lchild:
#             print(f'Second smallest value is {current.lchild.key}')
#         else:
#             print('Tree has less than 2 nodes')

# # Example usage:
# root = TreeNode(5)
# root.lchild = TreeNode(3)
# root.rchild = TreeNode(7)
# root.lchild.lchild = TreeNode(2)
# root.lchild.rchild = TreeNode(4)

# # Call the min_node method to find the second smallest node
# root.min_node()  # Output: Second smallest value is 3




# class TreeNode:
#     def __init__(self, key):
#         self.key = key
#         self.left = None
#         self.right = None

# def find_smallest_node(self):
#     current = self
#     while current.left:
#         current = current.left
#     return current

# # Example usage:
# # Constructing a sample binary search tree
# root = TreeNode(10)
# root.left = TreeNode(5)
# root.right = TreeNode(15)
# root.left.left = TreeNode(2)
# root.left.right = TreeNode(7)

# # Find the smallest node in the BST
# smallest_node = find_smallest_node(root)
# print("Smallest node in the BST:", smallest_node.key)  # Output: Smallest node in the BST: 2
