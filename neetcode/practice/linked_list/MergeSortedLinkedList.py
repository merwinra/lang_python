from neetcode.practice.linked_list.ListNode import ListNode

class MergeSortedLinkedList:
    def mergeTwoLists(head1: ListNode, head2: ListNode) -> ListNode:
        dummy = node = ListNode()

        while head1 and head2:
            if head1.val < head2.val:
                node.next = head1
                head1 = head1.next
            else:
                node.next = head2
                head2 = head2.next
            node = node.next
        
        if head1:
            node.next = head1
        else:
            node.next = head2
        
        return dummy.next