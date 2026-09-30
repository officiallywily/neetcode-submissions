# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        
        curr1, curr2 = list1, list2
        
        dummy_node = ListNode()
        head = dummy_node

        while curr1 and curr2:
            if curr1.val < curr2.val:
                head.next = curr1
                head = head.next
                curr1 = curr1.next
            else:
                head.next = curr2
                head = head.next
                curr2 = curr2.next
            
        if curr1:
            head.next = curr1
        elif curr2:
            head.next = curr2
        
        return dummy_node.next