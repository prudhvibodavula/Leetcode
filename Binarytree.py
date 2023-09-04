#Depth of a node: defined as the number of edges in the path from the root of the tree to the node.
#Height of a node: The height of a node can be defined as the length of the longest path from the node to a leaf node of the tree.
#Height of the Tree: The height of a tree is the length of the longest path from the root of the tree to a leaf node of the tree.
#Degree of a Node: The total count of subtrees attached to that node is called the degree of the node. 
#The degree of a leaf node must be 0. The degree of a tree is the maximum degree of a node among all the nodes in the tree.
class Node:
    def __init__(self,data) :
        self.data=data
        self.left=None
        self.right=None
class BinaryTree:
    def __init__(self,root):
        self.root=Node(root)

    def print_traversal(self,type):
        if type=="preorder":
            return self.preorder(bt.root,"")
        if type=="inorder":
            return self.inorder(bt.root,"")
        if type=="postorder":
            return self.postorder(bt.root,"")
    def preorder(self,start,traversal):
        if start:
            traversal+=(str(start.data)+"-")
            traversal=self.preorder(start.left,traversal)
            traversal=self.preorder(start.right,traversal)
        return traversal
    def inorder(self,start,traversal):
        if start:
            
            traversal=self.inorder(start.left,traversal)
            traversal+=(str(start.data)+"-")
            traversal=self.inorder(start.right,traversal)
        return traversal
    def postorder(self,start,traversal):
        if start:
            
            traversal=self.postorder(start.left,traversal)
            traversal=self.postorder(start.right,traversal)
            traversal+=(str(start.data)+"-")
        return traversal
bt=BinaryTree(1)
bt.root.left=Node(2)
bt.root.left.left=Node(4)
bt.root.left.right=Node(5)
bt.root.right=Node(3)
bt.root.right.left=Node(6)
bt.root.right.right=Node(7)
print(bt.print_traversal("preorder"))
print(bt.print_traversal("inorder"))
print(bt.print_traversal("postorder"))