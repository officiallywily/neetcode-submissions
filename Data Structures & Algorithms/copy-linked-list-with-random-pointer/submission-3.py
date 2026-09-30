"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        node_map: Dict["node": "node"] = {}
        curr = head
        while curr:
            new_node = Node(curr.val)
            node_map[curr] = new_node
            curr = curr.next
        
        curr = head
        while curr:
            node_map[curr].next = node_map.get(curr.next, None)
            node_map[curr].random = node_map.get(curr.random, None)
            curr = curr.next
        
        return node_map[head]
