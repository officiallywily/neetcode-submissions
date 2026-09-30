# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return None
        # separate first and second halves
        slow, fast = head, head.next # head.next for fast ensures slow ends up as last element of first half
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse the second half and sever first half
        curr = slow.next
        slow.next = None
        prev = None
        while curr:
            tmp_next = curr.next
            curr.next = prev
            prev = curr
            curr = tmp_next

        # zipper merge

        first, second = head, prev
        
        while second:
            # hold the values
            tmp_first = first.next
            tmp_second = second.next

            # merge
            first.next = second
            second.next = tmp_first

            # shift values for next iteration
            first = tmp_first
            second = tmp_second

