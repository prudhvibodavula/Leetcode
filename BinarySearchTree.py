#Insert a node into a BST: A new key is always inserted at the leaf. 
#Start searching a key from the root till a leaf node. Once a leaf node is found, the new node is added as a child of the leaf node.

class Node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None

def insert(node,key): 
    #tree empty return new node
    if node is None:
        return Node(key)
    
    if key < node.key:
        node.left = insert(node.left,key)
    elif key > node.key:
        node.right = insert(node.right,key)
    return node

# Function to create a new BST node
def newNode(item):
    temp = Node(item)
    temp.key = item
    temp.left=temp.right=None
    return temp

# traversal of the bst
def inorder(root):
    if root:
        inorder(root.left)
        print(root.key,end=" ")
        inorder(root.right)

def preorder(root):
    if root:
        print(root.key,end=" ")
        preorder(root.left)
        preorder(root.right)
"""
    Let us create following BST
          50
       /     \
      30      70
     /  \    /  \
    20  40  60   80
"""

root = None
keys=[50, 30, 20, 40, 70, 60, 80]
for key in keys:
    root = insert(root,key)
inorder(root)
print("")
preorder(root)
#Time Complexity: O(N), where N is the number of nodes of the BST 
#Auxiliary Space: O(1) 
# Inorder traversal: In case of binary search trees (BST), Inorder traversal gives nodes in non-decreasing order. 
# We visit the left child first, then the root, and then the right child.

# Preorder traversal: Preorder traversal first visits the root node and then traverses the left and the right subtree. \
# It is used to create a copy of the tree. Preorder traversal is also used to get prefix expression on of an expression tree.

#Postorder traversal: Postorder traversal first traverses the left and the right subtree and then visits the root node.\
#  It is used to delete the tree. In simple words, visit the root of every subtree last.
