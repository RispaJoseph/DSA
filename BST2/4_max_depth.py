class Node:
	def __init__(self, key):
		self.data = key
		self.left = None
		self.right = None
		
def max_depth(root):
	if root is None:
		return 0
	return 1 + max(max_depth(root.left),max_depth(root.right))
	
		

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print(max_depth(root))