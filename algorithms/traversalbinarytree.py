class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

# Insert Node to keep order in data
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

# Print the Tree
    def PrintTree(self,indent = 0):
        s = " " * indent
        print(s + str(self.data))
        if self.left:
            self.left.PrintTree(indent = indent + 2)
        if self.right:
            self.right.PrintTree(indent = indent + 2)

# Inorder traversal
# Left -> Root -> Right
    def InOrderTraversal(self, root):
        res = []
        if root:
            res = self.InOrderTraversal(root.left)
            res.append(root.data)
            res = res + self.InOrderTraversal(root.right)
        return res
# Preorder traversal
# Root -> Left ->Right
    def PreOrderTraversal(self, root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.PreOrderTraversal(root.left)
            res = res + self.PreOrderTraversal(root.right)
        return res
# Postorder traversal
# Left ->Right -> Root
    def PostOrderTraversal(self, root):
        res = []
        if root:
            res = self.PostOrderTraversal(root.left)
            res = res + self.PostOrderTraversal(root.right)
            res.append(root.data)
        return res

root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(31)
root.insert(19)
root.insert(30)
root.insert(42)
print(root.InOrderTraversal(root))
root.PrintTree()
print(root.PreOrderTraversal(root))
print(root.PostOrderTraversal(root))
