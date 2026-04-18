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
        new_head = Node(0)
        new_curr = new_head
        curr = head

        while new_curr and curr:
            temp = Node(curr.val)
            new_curr.next = temp
            new_curr = new_curr.next
            curr = curr.next

        dct = {}
        curr = head
        new_curr = new_head.next
        while curr and new_head:
            dct[curr] = new_curr
            new_curr = new_curr.next
            curr = curr.next

        curr = head
        new_curr = new_head.next
        while curr and new_head:
            new_curr.random = dct[curr.random] if curr.random else None
            curr = curr.next
            new_curr = new_curr.next

        return new_head.next
