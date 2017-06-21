'''
Binary tree data structure interpretation 
'''

#Binary tree node with left and right tree
class binaryTreeNode:

    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

    #Prints node value
    def visit(self):
        print(self.value)

#Add value to binary tree by going left if smaller or right if larger
def addBinarySearchChild(node,newValue):
    #If value already in tree, do nothing
    if node.value != newValue:
        #If value smaller than value, go left, else go right
        #If left or right don't exist, create them and use the current value
        if newValue < node.value:
            if node.left == None:
                node.left = binaryTreeNode(newValue)
            
            else:
                addBinarySearchChild(node.left,newValue)
        
        if newValue > node.value:
            if node.right == None:
                node.right = binaryTreeNode(newValue)
            
            else:
                addBinarySearchChild(node.right,newValue)       
                

#Left branch is visited, then right
def inOrderTransversal(node):
    if node != None:
        inOrderTransversal(node.left)
        node.visit()
        inOrderTransversal(node.right)

#Current node is visited before children nodes
def preOrderTransversal(node):
    if node != None:
        node.visit()
        preOrderTransversal(node.left)
        preOrderTransversal(node.right)

#First children nodes are visited, then current node
def postOrderTransversal(node):
    if node != None:
        postOrderTransversal(node.left)
        postOrderTransversal(node.right)
        node.visit()
       