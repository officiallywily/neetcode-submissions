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
    
        trailer = ListNode()
        trailer.next = head
        dummy = trailer
        while leader:
            leader = leader.next
            trailer = trailer.next
        
        if trailer.next:
            trailer.next = trailer.next.next
        
        return dummy.next

        