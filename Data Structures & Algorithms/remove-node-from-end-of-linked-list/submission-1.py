# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first = head
        count = 0
        while count<n:
            count+=1
            first = first.next

        if not first:
            return head.next

        second = head
        while first.next:
            second = second.next
            first = first.next

        print(second.val)
        second.next = second.next.next
        return head