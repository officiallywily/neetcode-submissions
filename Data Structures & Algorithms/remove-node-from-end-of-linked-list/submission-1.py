# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # edge case
        if not head:
            return head

        # offset
        leader = head
        for i in range(n):
            if not leader:
                return head
            leader = leader.next

        # if n = length of linked list (remove first element)
        if not leader:
            return head.next

        trailer = head
        prev = None
        while leader:
            leader = leader.next
            prev = trailer
            trailer = trailer.next
        
        if prev.next:
            prev.next = prev.next.next
        
        return head

        
        # head=[1,2]
        # n=2


            
            