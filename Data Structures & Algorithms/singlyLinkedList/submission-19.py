class LinkedList:
    class Node:
        def __init__(self, value, nextNode = None):
            self._value = value
            self._next = nextNode

        def getVal(self):
            return self._value

        def getNext(self):
            return self._next
    
    def __init__(self):
        self._numItems: int = 0
        self._head = None
    
    def get(self, index: int) -> int:
        if index >= self._numItems:
            return -1
        currNode = self._head
        i = 0
        while i != index:
            currNode = currNode.getNext()
            i += 1
        return currNode.getVal()
        
    def insertHead(self, val: int) -> None:
        newHead = self.Node(value=val, nextNode=self._head)
        self._numItems += 1
        self._head = newHead

    def insertTail(self, val: int) -> None:
        if not self._head:
            self.insertHead(val)
            return
        currNode = self._head
        while currNode._next:
            currNode = currNode.getNext()
        currNode._next = self.Node(value=val)
        self._numItems += 1

    def remove(self, index: int) -> bool:
        if index >= self._numItems:
            return False
        if index == 0:
            self._head = self._head._next
            self._numItems -= 1
            return True
        
        i = 0
        currNode = self._head
        while i + 1 < index:
            currNode = currNode._next
            i += 1
        
        currNode._next = currNode._next._next
        self._numItems -= 1
        return True
        

    def getValues(self) -> List[int]:
        if not self._head:
            return []
        values = list[int]()

        currNode = self._head
        values.append(currNode.getVal())
        while currNode._next:
            currNode = currNode._next
            values.append(currNode.getVal())
        return values
