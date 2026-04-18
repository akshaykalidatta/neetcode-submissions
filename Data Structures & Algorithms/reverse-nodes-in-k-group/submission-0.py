# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self, head: Optional[ListNode]) -> (Optional[ListNode], Optional[ListNode]):
        curr = head
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev, head

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #iterate through list k times, disconnect list then reverse and connect back
        new_head = ListNode(0)
        curr = khead = head
        new_head.next = head
        prev_tail = new_head

        while curr:
            cnt = 0
            while cnt < k-1 and curr.next:
                curr = curr.next
                cnt +=1

            if cnt < k-1:
                prev_tail.next = khead
                break

            temp = curr.next if curr.next else None
            curr.next = None
            khead, ktail = self.reverse(khead)
            prev_tail.next = khead
            prev_tail = ktail
            ktail.next = temp
            curr = khead = temp
            
        return new_head.next

        