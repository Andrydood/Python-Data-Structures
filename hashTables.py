'''
Hash table data structure implementation
'''

#Decode string into its hashcode
def stringHashCode(inputString):
    
    #Done by converting each character to its unicode value and adding them all together
    outHash = 0

    for i,c in enumerate(inputString):
        outHash += ord(c)*(i+1)

    return outHash

class hashTable:

    def __init__(self,tableSize):
        #Initialise table as empty with 256 possible addresses
        self.tableSize = tableSize
        self.table = [[]]*tableSize
    
    def addItem(self,key,item):
        #Add item given a reference key. Key is calculated if it is a string
        if type(key)==str:
            index = stringHashCode(key)%self.tableSize
        else:
            index = key%self.tableSize

        self.table[index].append(item)
    
    def findItem(self,key):
        #Decode key and fetch item from table
        if type(key)==str:
            index = stringHashCode(key)%self.tableSize
        else:
            index = key%self.tableSize

        return self.table[index]