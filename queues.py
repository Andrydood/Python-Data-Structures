'''
Queue data structure implementation
'''

#Each item in the queue is a queue node
class queueNode:

    def __init__(self,value,nextNode):
        self.value = value
        self.nextNode = nextNode

class queue:

    def __init__(self):
        self.last = None
        self.first = None

    #If node is added to queue, it is set as the last node and as the "next node" for the previous last node.
    #If the queue is empty, it is also added as first node and not added as "next node" to anything
    def add(self,value):
        newNode = queueNode(value,None)

        if self.last == None:
            self.last = newNode
        else:
            self.last.nextNode = newNode
            self.last = newNode
        
        if self.first == None:
            self.first = newNode

    #If value is removed, the first node's value is output, and the next node is set as the first node
    def remove(self):
        if self.first == None:
            print("Queue is empty")
            return None
        
        firstValue = self.first.value
        self.first = self.first.nextNode
        return firstValue
    
    def isEmpty(self):
        return self.first == None
