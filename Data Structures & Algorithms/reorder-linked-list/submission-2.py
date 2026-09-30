# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
       
        # PHASE 1: finding the middle
        slow = head
        fast = head.next # ensures slow to be at the end of the first half

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # PHASE 2: reversing the second half
        curr = slow.next
        slow.next = None # sever the first half from the second half
        prev = None

        while curr:
            tmp_next = curr.next
            curr.next = prev
            prev = curr
            curr = tmp_next
        # prev is now the head of the reversed second half

        # PHASE 3: merge the two halves

        first = head
        second = prev
        while second:
            tmp_next1 = first.next
            tmp_next2 = second.next
            first.next = second
            second.next = tmp_next1
            first = tmp_next1
            second = tmp_next2

