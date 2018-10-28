# Tree Traversal Algorithm is the process of vissting each node of a binary tree exactly once.

class Node:
    def __init__(self,data):
        self.value = data
        self.left = None
        self.right = None

    def getValue(self):
        return self.value

    def addLeft(self,node):
        self.left = node

    def addRight(self,node):
        self.right = node

    def getRight(self):
        return self.right

    def getLeft(self):
        return self.left

    def PrintTree(self,indent = 0):
        s = " " * indent
        print(s + str(self.value))
        if self.left:
            self.left.PrintTree(indent = indent + 2)
        if self.right:
            self.right.PrintTree(indent = indent + 2)

    # Root -> Left ->Right 
    def PreOrderTraversal(self, nodes):
        nodes.append(self.getValue())
        if (self.getLeft() is not None):
            self.getLeft().PreOrderTraversal(nodes)
        if (self.getRight() is not None):
            self.getRight().PreOrderTraversal(nodes)

        return nodes

    # Left -> Right  -> Root
    def PostOrderTraversal(self, nodes):
        if (self.getLeft() is not None):
            self.getLeft().PreOrderTraversal(nodes)
        if (self.getRight() is not None):
            self.getRight().PreOrderTraversal(nodes)
        nodes.append(self.getValue())
        return nodes

# Tests start here
# Create a tree
root = Node(25)
n1 = Node(13)
n2 = Node(16)
n3 = Node(18)
n4 = Node(19)
root.addLeft(n1)
root.addRight(n2)
n1.addLeft(n3)
n1.addRight(n4)
n3.addLeft(Node(21))
n3.addRight(Node(23))
n2.addLeft(Node(27))

root.PrintTree()
print(root.PreOrderTraversal([]))
print(root.PostOrderTraversal([]))
