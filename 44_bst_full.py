class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert_recursive(self.root, key)

    def _insert_recursive(self, root, key):
        if root is None:
            return TreeNode(key)
        if key < root.key:
            root.left = self._insert_recursive(root.left, key)
        elif key > root.key:
            root.right = self._insert_recursive(root.right, key)
        return root

    def preorder(self):
        self._preorder_recursive(self.root)
        print()

    def _preorder_recursive(self, root):
        if root:
            print(root.key, end=" ")
            self._preorder_recursive(root.left)
            self._preorder_recursive(root.right)

    def inorder(self):
        self._inorder_recursive(self.root)
        print()

    def _inorder_recursive(self, root):
        if root:
            self._inorder_recursive(root.left)
            print(root.key, end=" ")
            self._inorder_recursive(root.right)

    def postorder(self):
        self._postorder_recursive(self.root)
        print()

    def _postorder_recursive(self, root):
        if root:
            self._postorder_recursive(root.left)
            self._postorder_recursive(root.right)
            print(root.key, end=" ")

    def delete(self, key):
        self.root = self._delete_recursive(self.root, key)

    def _delete_recursive(self, root, key):
        if root is None:
            return root

        if key < root.key:
            root.left = self._delete_recursive(root.left, key)
        elif key > root.key:
            root.right = self._delete_recursive(root.right, key)
        else:
            # Case 1: Node with only one child or no child
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp

            # Case 2: Node with two children
            # Get the inorder successor (smallest in the right subtree)
            temp = self._min_value_node(root.right)
            # Copy the inorder successor's content to this node
            root.key = temp.key
            # Delete the inorder successor
            root.right = self._delete_recursive(root.right, temp.key)

        return root

    def _min_value_node(self, node):
        current = node
        # Loop down to find the leftmost leaf
        while current.left is not None:
            current = current.left
        return current

# Example usage:
bst = BST()
bst.insert(50)
bst.insert(30)
bst.insert(20)
bst.insert(40)
bst.insert(70)
bst.insert(60)
bst.insert(80)

print("Inorder traversal:")
bst.inorder()

print("Preorder traversal:")
bst.preorder()

print("Postorder traversal:")
bst.postorder()

# Delete a node
bst.delete(30)
print("Inorder traversal after deletion of 30:")
bst.inorder()
