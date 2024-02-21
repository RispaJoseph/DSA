class TreeNode:
	def __init__(self, key):
		self.data = key
		self.left = None
		self.right = None
		
def min_depth(root):
	if root is None:
		return 0
	if root.left is None:
		return 1 + min_depth(root.right)
	if root.right is None:
		return 1 + min_depth(root.left)
	if root.left is None and root.right is None:
		return 1
	return 1 + min(min_depth(root.left),min_depth(root.right))
		

# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left = Node(4)
# root.left.right = Node(5)

root = TreeNode(2)
root.right = TreeNode(3)
root.right.right = TreeNode(4)
root.right.right.right = TreeNode(5)
root.right.right.right.right = TreeNode(6)

print(min_depth(root))
