'''
Implementation of min heap data structure
'''

#An array will be used to hold the data
#In this, [1] will be the root node
#For any node in index [i], the left child will be in position [2*i] and the right in [2*i +1]
#For any node [i], the parent will be in [i/2] (integer division)
#This makes it easy to find the next available position for a new node
class heap:

    def __init__(self):
        self.nodes = [0]

    #To insert a value, first it is added to the bottom most, right most position
    #Then, it is checked if the current node is less than the parent node, if so they swap position
    #This is done until it is no longer the case
    def insert(self,value):
        self.nodes.append(value)
        currentIndex = len(self.nodes) - 1
        parentIndex = currentIndex // 2

        while self.nodes[currentIndex] < self.nodes[parentIndex] and currentIndex != 1:
            bubbleSwap(self,currentIndex,parentIndex)

            currentIndex = parentIndex
            parentIndex = currentIndex // 2

    #Returns and removes minimum value from heap
    #First, root node is removed and swapped with the last element of the heap
    #Root node is then swapped with its children until the min heap property is restored
    #Node being passed down is substituted with lowest child value to keep min heap 
    def removeMinimum(self):
        minVal = self.nodes[1]
        self.nodes[1] = self.nodes.pop()
        currentPosition = 1
        leftChild = currentPosition*2
        rightChild = currentPosition*2 +1

        if leftChild <= (len(self.nodes) - 1):
            if  rightChild <= (len(self.nodes) - 1):

                while self.nodes[currentPosition] > self.nodes[leftChild] or  self.nodes[currentPosition] > self.nodes[rightChild]:

                    if self.nodes[leftChild] < self.nodes[rightChild]:
                        bubbleSwap(self,currentPosition,leftChild)
                        oldVal = leftChild

                    else:
                        bubbleSwap(self,currentPosition,rightChild)
                        oldVal = rightChild

                    currentPosition = oldVal
                    leftChild = oldVal*2
                    rightChild = oldVal*2 + 1 
                    
                    #If final node, then break, if there is only one node left, then check if needs switching, then break
                    if rightChild > (len(self.nodes) - 1):
                        if leftChild > (len(self.nodes) - 1):
                            break
                        
                        if self.nodes[currentPosition] > self.nodes[leftChild]:
                            bubbleSwap(self,currentPosition,leftChild)
                            break
                        else:
                            break
            
            #If there is only a left node after the root, see if it needs switching
            elif self.nodes[currentPosition] > self.nodes[leftChild]:
                bubbleSwap(self,currentPosition,leftChild)

#Swaps 2 nodes
def bubbleSwap(heap,index1,index2):
    buffer =heap.nodes[index1]
    heap.nodes[index1] = heap.nodes[index2]
    heap.nodes[index2] = buffer

