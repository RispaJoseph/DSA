# BST and insert object and search with objectId

class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def insert(root,data):
    if root is None:
        return TreeNode(data)
    
    if data['id'] < root.data['id']:
        root.left = insert(root.left,data)

    elif data['id'] > root.data['id']:
        root.right = insert(root.right,data)

    else:
        pass

    return root


def search(root,key):
    if root is None or root.data['id'] == key:
        return root
    if key < root.data['id']:
        return search(root.left,key)
    else:
        return search(root.right,key)




root = None
root = insert(root,{'id':101, 'name':'Rue', 'age':27})
root = insert(root,{'id':102, 'name':'Maddy', 'age':32})
root = insert(root,{'id':103, 'name':'Lexi', 'age':24})


search_id = 101
result = search(root,search_id)

if result:
    print()
    print("Data found")
    print("ID:", result.data['id'])
    print("Name:", result.data['name'])
    print("Age:", result.data['age'])
    print()
else:
    print("Data not found!")


