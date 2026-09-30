# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head
        isOdd = False

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # if fast is not None, slow is the dead center and must be moved
        if fast:
            isOdd = True
            head2 = slow.next
        # slow is either the dead center, or beginning of second half
        else:
            head2 = slow
        
        # reverse the second half first
        prev, curr = None, head2
        while curr:
            tmp_next = curr.next
            curr.next = prev
            prev = curr
            curr = tmp_next
        # curr is now the head of the reversed second half

        curr2 = prev
        curr1 = head
        dummy_node = ListNode()
        trav = dummy_node
        while curr2:
            tmp_next1 = curr1.next
            tmp_next2 = curr2.next
            trav.next = curr1
            trav.next.next = curr2
            trav = trav.next.next
            curr2 = tmp_next2
            curr1 = tmp_next1

        if isOdd:
            trav.next = curr1
            trav = trav.next
        
        trav.next = None
        

        

        
