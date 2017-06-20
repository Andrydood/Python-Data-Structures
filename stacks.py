'''
Stack data structure implementation
'''

#Each item within the stack class will be a stack node
class stackNode:

    def __init__(self,value,nextNode):
        self.value = value
        self.next = nextNode


#Stack class
class stack:

    #Initiate empty stack with None as top node
    def __init__(self):
        self.top = None
    
    #If a value is pushed onto the stack, a new node is initiated, the current top is set 
    #as the new node's "next", and the new node is set as the new top
    def push(self,value):
        nextNodeBuffer = self.top
        self.top = stackNode(value,nextNodeBuffer)

    #The pop function returns the top value of the stack and removes it from the stack
    #Done by reading the value, setting the new top node as the previous top's next node and deleting the previous top node
    def pop(self):
        if self.top == None:
            print("Stack is empty")
            return None

        output = self.top.value
        nextNodeBuffer = self.top.next
        self.top = nextNodeBuffer
        return output
    
    #Like pop but node is not deleted
    def peek(self):
        if self.top == None:
            print("Stack is empty")
            return None

        return self.top.value

    #Checks if stack is empty
    def isEmpty(self):
        return self.top == None