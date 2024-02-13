class Treenode:
    def __init__(self,value):
        self.val = value
        self.left = None
        self.right = None

class Solution:
    
    def Inordertraversal(self,root):
        res = []

        if root is None:
            return res
        
        A = self.Inordertraversal(root.left)
        res.extend(A)
        res.append(root.val)
        B = self.Inordertraversal(root.right)
        res.extend(B)

        return res
    

    def PreorderTraversal(self,root):
        res = []

        if root is None:
            return []
        res.append(root.val)
        A = self.PreorderTraversal(root.left)
        res.extend(A)
        B = self.PreorderTraversal(root.right)
        res.extend(B)

        return res
    

    def PostorderTraversal(self,root):
        res = []

        if root is None:
            return []
        A = self.PostorderTraversal(root.left)
        res.extend(A)
        B = self.PostorderTraversal(root.right)
        res.extend(B)
        res.append(root.val)

        return res 



    

    

root = Treenode(5)
root.left = Treenode(3)
root.right = Treenode(7)
root.left.left = Treenode(2)
root.left.right = Treenode(4)
root.right.left = Treenode(6)
root.right.right = Treenode(8)

solution = Solution()

print("Inorder Traversal = ",solution.Inordertraversal(root))
print("Preorder traversal = ",solution.PreorderTraversal(root))
print("Postorder Traversal = ",solution.PostorderTraversal(root))


#.............. output...................
# Inorder Traversal: [2, 3, 4, 5, 6, 7, 8]
# Preorder Traversal: [5, 3, 2, 4, 7, 6, 8]
# Postorder Traversal: [2, 4, 3, 6, 8, 7, 5]
