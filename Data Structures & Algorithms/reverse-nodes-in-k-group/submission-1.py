class Solution:
    def reverse(self, head: Optional[ListNode]) -> (Optional[ListNode], Optional[ListNode]):
        curr, prev = head, None
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        return prev, head

    def getKth(self, node: Optional[ListNode], k: int) -> Optional[ListNode]:
        while node and k > 1:
            node = node.next
            k -= 1
        return node

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        new_head = ListNode(0)
        new_head.next = head
        prev_tail = new_head

        while True:
            curr = self.getKth(prev_tail.next, k)
            if not curr:
                break

            khead = prev_tail.next
            temp = curr.next
            curr.next = None

            khead, ktail = self.reverse(khead)
            prev_tail.next = khead
            ktail.next = temp
            prev_tail = ktail

        return new_head.next