class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def printInorder(root):
    if root:
        printInorder(root.left)
        print(root.val),
        printInorder(root.right)

def printPostorder(root):
    if root:
        printPostorder(root.left)
        printPostorder(root.right)
        print(root.val),


def printPreorder(root):
    if root:
        print(root.val),
        printPreorder(root.left)
        printPreorder(root.right)


root = Node(0)
root.right = Node('P')
root.right.left = Node(0)
root.right.left.right = Node(0)
root.right.left.right.right = Node(0)
root.right.left.right.right.right = Node(0)
root.right.left.right.right.right.right = Node(0)
root.right.right = Node('T')
root.right.right.left = Node('S')
root.right.right.left.left = Node('Q')
root.right.right.left.left.right = Node('R')
root.right.right.right = Node('X')
root.right.right.right.left = Node('U')
root.right.right.right.left.right = Node('W')
root.right.right.right.left.right.left = Node('V')
root.right.right.right.right = Node('Y')

print("Preorder traversal of binary tree is")
printPreorder(root)

print("\nInorder traversal of binary tree is")
printInorder(root)

print("\nPostorder traversal of binary tree is")
printPostorder(root)
