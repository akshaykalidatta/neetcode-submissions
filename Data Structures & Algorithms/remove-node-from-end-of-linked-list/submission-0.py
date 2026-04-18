# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        curr = head
        while curr:
            count+=1
            curr=curr.next

        element = count - n
        if element == 0:
            return head.next
        count = 0
        curr = head
        while curr:
            if count == element-1:
                curr.next = curr.next.next
                break
            curr = curr.next
            count+=1

        return head

