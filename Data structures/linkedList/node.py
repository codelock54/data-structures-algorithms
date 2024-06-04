class Node():
    def __init__(self,value):
        self.value = value
        self.next = None

    def getNext(self):
        return self.next
    
    def getValue(self):
        return self.value   
    
    def setValue(self, value):
        self.value = value 

    def setNext(self, node):
        self.next = node

    def __str__(self):
        return str(self.value)
        