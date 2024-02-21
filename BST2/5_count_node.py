class Node:
	def __init__(self, key):
		self.data = key
		self.left = None
		self.right = None
		
def inorder(root):
	if root is None:
		return []
	return 1 + (inorder(root.left) if root.left else 0) + (inorder(root.right) if root.right else 0)



root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print(inorder(root))