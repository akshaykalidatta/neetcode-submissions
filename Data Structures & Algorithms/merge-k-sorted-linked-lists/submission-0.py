# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def merge2Lists(self, lists1: Optional[ListNode], lists2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0)
        curr = head
        while lists1 and lists2:
            if lists1.val < lists2.val:
                curr.next = lists1
                lists1 = lists1.next
            else:
                curr.next = lists2
                lists2 = lists2.next

            curr = curr.next

        while lists1:
            curr.next = lists1
            lists1 = lists1.next
            curr = curr.next

        while lists2:
            curr.next = lists2
            lists2 = lists2.next
            curr = curr.next

        return head.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists: return None
        k = len(lists)
        for i in range(1, k):
            lists[i] = self.merge2Lists(lists[i-1], lists[i])

        return lists[k-1]