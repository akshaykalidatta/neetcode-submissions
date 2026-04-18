# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #get half of the list
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None
        #reverse the list
        prev = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        #merge them
        curr = head
        while curr and prev:
            temp = curr.next
            temp2 = prev.next
            curr.next = prev
            prev.next = temp 
            curr = temp
            prev = temp2

        head = curr

