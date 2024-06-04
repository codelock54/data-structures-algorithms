from linkedList.node import Node


class linkedList:
    def __init__(self):
        self.head = None

    def getHead(self):
        return self.head

    def setHead(self, head):
        self.head = head

    # def add(self, item):
    #     p = Node(item)

    #     if self.head is None:
    #         self.head = p

    #     else:
    #         p.setNext(self.head)
    #         self.head = p

    def addFinal(self, item):
        p = Node(item)
        if self.head is None:
            self.head = p
        else:
            self.head.setNext(p)

    def printList(self):
        t = self.head
        while t is not None:
            print(t, end=", ")
            t = t.getNext()
        # print()

    def delete(self, val):
        current = self.head
        previous = None

        while current != None:
            if current.getValue() == val:
                if previous != None:
                    previous.setNext(current.getNext())

                else:
                    self.head = current.getNext()

                current.setNext(None)
                return True

        return False
