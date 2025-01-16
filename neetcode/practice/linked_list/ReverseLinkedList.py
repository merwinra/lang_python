from neetcode.practice.linked_list import ListNode
from typing import Optional

class ReverseLinkedList:
    def reverseLinkedListIteratively(this, head: ListNode) -> ListNode:
        prev = None
        curr = head

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        return prev
    
    def reverseLinkedListRecursively(this, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        newHead = head
        if head.next:
            newHead = this.reverseLinkedListRecursively(head.next)
            head.next.next = head
        head.next = None
        
        return newHead
