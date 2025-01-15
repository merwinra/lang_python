import ListNode

class SinglyLinkedList:
    def __init__(this):
        this.head = None
        this.tail = None
        this.size = 0
    
    def insertIntoAnEmptyList(this, node: ListNode) -> None:
        this.head = this.tail = ListNode(node)
        this.size += 1
        return

    def insertAtStart(this, val: int) -> None:
        node = ListNode(val)
        
        if this.head == None:
            this.insertIntoAnEmptyList(node)
        
        else:
            node.next = this.head
            this.head = node
        
        this.size += 1
        return
    
    def insertAtEnd(this, val: int) -> None:
        node = ListNode(val)

        if this.head == None:
            this.insertIntoAnEmptyList(node)
        
        else:
            this.tail.next = node
            this.tail = node

        this.size += 1
        return
    
    def getNodeAtIndex(this, index: int) -> ListNode:
        if index < 0 or index >= this.size:
            print("Index out of bounds")
        
        curr = this.head
        for i in range(index):
            curr = curr.next
        return curr

    def removeAtIndex(this, index: int) -> None:
        if index < 0 or index >= this.size:
            print("Index out of bounds")
            return

        if index == 0:
            this.head = this.head.next
            if this.head == None:
                this.tail = None
        
        else:
            prev = this.getNodeAtIndex(index)
            toRemove = prev.next

            prev.next = toRemove.next

            if toRemove == this.tail:
                this.tail = prev
        
        this.size -= 1
        return
    
    def printList(this) -> None:
        curr = this.head
        while curr != None:
            print(curr.val, " -> ", end = "")
            curr = curr.next
        print()