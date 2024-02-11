class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def searchBST(self, root, val):
        if root is None or root.val == val:
            return root
        elif val < root.val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)

    # def subtreeSearch(self, root, val):
    #     result_node = self.searchBST(root, val)
    #     if result_node:
    #         return self.collectSubtreeValues(result_node)
    #     else:
    #         return None  # Node with value val not found in the BST

    # def collectSubtreeValues(self, root):
    #     values = []
    #     if root:
    #         # Inorder traversal to collect values
    #         self._collectSubtreeValues(root, values)
    #     return values

    # def _collectSubtreeValues(self, root, values):
    #     if root:
    #         values.append(root.val)
    #         self._collectSubtreeValues(root.left, values)
    #         self._collectSubtreeValues(root.right, values)

solution = Solution()



# Example usage:
# Create a BST
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

# Create a Solution instance
solution = Solution()
search_value = 100
result = solution.searchBST(root,search_value)



# Search for a value in the BST
# search_value = 4
# result_values = solution.subtreeSearch(root, search_value)

# if result_values is not None:
#     print("Values in the subtree rooted at the node with value", search_value)
#     print(result_values)
# else:
#     print(f"Node with value {search_value} not found in the BST")
