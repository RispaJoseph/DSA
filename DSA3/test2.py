# #{
# id: 101,
# name: "Rispa",
# age: 22
# }

# search by id: 101 and output will be 
#  {
# id: 101,
# name: "Rispa",
# age: 22
# }

# class TreeNode:
#     def __init__(self,value):
#         self.val = value
#         self.left = None
#         self.right = None
    
# def search_id(root):
#     def traverse(node):
#         if node is None:
#             return []
#         return traverse(node.left)+[node.val]+traverse(node.right)
    
#     sequence = traverse(root)
#     for i in range(1,len(sequence)):
#         if i == root:
#             print("The data is",sequence[i])
#         else:
#             print("Data not found!")




# (){}[]
# (}(]


# list = []




# class TreeNode:
#     def __init__(self, key, val):
#         self.left = None
#         self.right = None
#         self.key = key
#         self.val = val

# class BST:
#     def __init__(self):
#         self.root = None

#     def insert(self, key, val):
#         self.root = self._insert_recursive(self.root, key, val)

#     def _insert_recursive(self, node, key, val):
#         if node is None:
#             return TreeNode(key, val)
#         if key < node.key:
#             node.left = self._insert_recursive(node.left, key, val)
#         elif key > node.key:
#             node.right = self._insert_recursive(node.right, key, val)
#         else:
#             node.val = val
#         return node

#     def search(self, key):
#         return self._search_recursive(self.root, key)

#     def _search_recursive(self, node, key):
#         if node is None or node.key == key:
#             return node
#         if key < node.key:
#             return self._search_recursive(node.left, key)
#         return self._search_recursive(node.right, key)

# # Example usage:
# bst = BST()
# bst.insert(5, "Object A")
# bst.insert(3, "Object B")
# bst.insert(7, "Object C")
# bst.insert(1, "Object D")
# bst.insert(4, "Object E")
# bst.insert(6, "Object F")
# bst.insert(9, "Object G")

# # Search for an object by its ID
# search_id = 4
# result_node = bst.search(search_id)
# if result_node:
#     print(f"Object found: {result_node.val}")
# else:
#     print(f"Object with ID {search_id} not found")





class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = TreeNode(data)
        else:
            self._insert_recursive(self.root, data)

    def _insert_recursive(self, node, data):
        if data['id'] < node.data['id']:
            if node.left is None:
                node.left = TreeNode(data)
            else:
                self._insert_recursive(node.left, data)
        elif data['id'] > node.data['id']:
            if node.right is None:
                node.right = TreeNode(data)
            else:
                self._insert_recursive(node.right, data)
        else:
            # ID already exists, handle accordingly (replace/update or ignore)
            pass

    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        if node is None or node.data['id'] == key:
            return node
        if key < node.data['id']:
            return self._search_recursive(node.left, key)
        return self._search_recursive(node.right, key)

# Example usage:
bst = BST()

# Insert data into the BST
bst.insert({'id': 101, 'name': 'John Doe', 'age': 38})
bst.insert({'id': 102, 'name': 'Daryl Dixon', 'age': 45})
bst.insert({'id':103, 'name':'Rick Grimes', 'age':43})

# Search for data by ID
search_id = 101
result_node = bst.search(search_id)
if result_node:
    print("Data found:")
    print("ID:", result_node.data['id'])
    print("Name:", result_node.data['name'])
    print("Age:", result_node.data['age'])
else:
    print(f"Data with ID {search_id} not found")

