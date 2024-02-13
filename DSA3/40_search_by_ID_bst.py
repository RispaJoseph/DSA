class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    # ensures that when a new instance of the BST class is created, 
    # it starts with an empty tree (i.e., no nodes).
    def __init__(self):
        self.root = None                        


    def insert(self, data):
        if not self.root:
            self.root = TreeNode(data)
        else:
            self.insert_recursive(self.root, data)

    def insert_recursive(self, node, data):
        if data['id'] < node.data['id']:
            if node.left is None:
                node.left = TreeNode(data)
            else:
                self.insert_recursive(node.left, data)
        elif data['id'] > node.data['id']:
            if node.right is None:
                node.right = TreeNode(data)
            else:
                self.insert_recursive(node.right, data)
        else:
            # ID already exists, handle accordingly (replace/update or ignore)
            pass

    def search(self, key):
        return self.search_recursive(self.root, key)

    def search_recursive(self, node, key):
        if node is None or node.data['id'] == key:
            return node
        if key < node.data['id']:
            return self.search_recursive(node.left, key)
        return self.search_recursive(node.right, key)

# Example usage:
bst = BST()

# Insert data into the BST
bst.insert({'id': 101, 'name': 'John Doe', 'age': 38})
bst.insert({'id': 102, 'name': 'Daryl Dixon', 'age': 45})
bst.insert({'id':103, 'name':'Rick Grimes', 'age':43})

# Search for data by ID
search_id = 102
result_node = bst.search(search_id)
if result_node:
    print("Data found:")
    print("ID:", result_node.data['id'])
    print("Name:", result_node.data['name'])
    print("Age:", result_node.data['age'])
else:
    print(f"Data with ID {search_id} not found")
