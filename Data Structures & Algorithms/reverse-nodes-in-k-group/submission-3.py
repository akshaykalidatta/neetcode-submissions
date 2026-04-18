# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self, head: Optional[ListNode]) -> (Optional[ListNode], Optional[ListNode]):
        curr, prev = head, None
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        return prev, head

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        new_head = ListNode(0)
        prev_tail = new_head
        curr = khead = head
        new_head.next = head

        while True:
            cnt = 0
            while curr and cnt < k-1:
                curr = curr.next
                cnt += 1

            if not curr or cnt < k-1:
                prev_tail.next = khead
                break

            temp = curr.next
            curr.next = None
            khead, ktail = self.reverse(khead)

            prev_tail.next = khead
            ktail.next = temp
            prev_tail = ktail

            curr = khead = temp

        return new_head.next
        