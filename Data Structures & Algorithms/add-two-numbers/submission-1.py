# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carryover = 0
        dummy = ListNode()
        sum_list = dummy
        while l1 or l2:
            l1val = 0
            l2val = 0
            if l1:
                l1val = l1.val
            if l2:
                l2val = l2.val
            node_sum = l1val + l2val + carryover
            carryover = node_sum // 10
            node_sum %= 10
            new_node = ListNode(node_sum)
            sum_list.next = new_node
            sum_list = sum_list.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carryover:
            new_node = ListNode(1)
            sum_list.next = new_node
        
        return dummy.next
