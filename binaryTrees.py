'''
Binary tree data structure interpretation 
'''

#Binary tree node with left and right tree. All the functions of a tree can 
#be controlled using the root node
class binaryTreeNode:

    def __init__(self,value,parent = None):
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent

    #Prints node value
    def visit(self):
        print(self.value)

'''
Binary search tree functions
'''
#Add value to binary tree by going left if smaller or right if larger
def addBinarySearchChild(node,newValue):
    #If value already in tree, do nothing
    if node.value != newValue:
        #If value smaller than value, go left, else go right
        #If left or right don't exist, create them and use the current value
        if newValue < node.value:
            if node.left == None:
                node.left = binaryTreeNode(newValue,node)
            
            else:
                addBinarySearchChild(node.left,newValue)
        
        if newValue > node.value:
            if node.right == None:
                node.right = binaryTreeNode(newValue,node)
            
            else:
                addBinarySearchChild(node.right,newValue)       
                
#Remove binary search node
def removeBinarySearchNode(node):
    #If node is leaf, just remove it
    if node.right == None and node.left == None: 
        if node.value < node.parent.value:
            node.parent.left = None

        else:
            node.parent.right = None
    
    #If node only has one child, connect the parent and child
    elif node.right != None and node.left == None: 
        if node.right.value < node.parent.value:
            node.parent.left = node.right
            node.right.parent = node.parent.left

        else:
            node.parent.right = node.right
            node.right.parent = node.parent.right

    elif node.right == None and node.left != None: 
        if node.left.value < node.parent.value:
            node.parent.left = node.left
            node.left.parent = node.parent.left

        else:
            node.parent.right = node.left
            node.left.parent = node.parent.right
                
    #If node has two children, find the lowest value in the right branch, replace
    #the current node's value with that value and remove the node with the  node with the lowest value in the right branch
    elif node.right != None and node.left != None: 
        minNode = minValue(node.right)
        node.value = minNode.value
        removeBinarySearchNode(minNode)

#Returns minimum value from branch
def minValue(node):
    if node.left == None:
        return node
    else:
        minRightValue(node.left)

'''
Tree transversal functions
'''
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
