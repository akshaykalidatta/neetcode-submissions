# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        if list1.val < list2.val:
            curr = list1
            list1 = list1.next
        else:
            curr = list2
            list2 = list2.next
        head = curr
        while list1 is not None and list2 is not None:
            print(curr.val)
            if list2.val < list1.val:
                curr.next = list2
                list2 = list2.next
            else:
                curr.next = list1
                list1 = list1.next
            curr = curr.next

        while list1 is not None:
            curr.next = list1
            list1 = list1.next
            curr = curr.next

        while list2 is not None:
            curr.next = list2
            list2 = list2.next
            curr = curr.next

        return head
            