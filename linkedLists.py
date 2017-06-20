'''
Linked list data structure implementation
'''

class Node:
    
    #Class is controlled by initial node. Initialised with value and itself as end node
    def __init__(self,value):
        self.value = value
        self.nextNode = None
        self.previousNode = None
    
    #If value is to be appended, iterate through nodes until final node is found and new node is added
    #Node is final if nextNode is set to None
    def append(self,value):
        finalNode = self
        while finalNode.nextNode != None:
            finalNode = finalNode.nextNode
        
        finalNode.nextNode = Node(value)
        finalNode.nextNode.previousNode = finalNode
    
    #Remove node by joining the next and previous nodes
    def remove(self):
        if self.previousNode != None:
            self.previousNode.nextNode = self.nextNode
        if self.nextNode != None:
            self.nextNode.previousNode = self.previousNode
        
    #Counts how many nodes are in the linked list
    def size(self):
        count = 1
        finalNode = self
        while finalNode.nextNode != None:
            finalNode = finalNode.nextNode
            count = count +1

        return count

