# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1, curr2 = l1, l2
        carry = 0
        head = ListNode(0)
        temp = head
        while curr1 and curr2:
            new_val = curr1.val + curr2.val + carry
            carry = 0
            if new_val > 9:
                carry = 1
                new_val = new_val%10
            temp.next = ListNode(new_val)
            temp = temp.next
            curr1 = curr1.next
            curr2 = curr2.next

        while curr1:
            new_val = curr1.val + carry
            carry = 0
            if new_val > 9:
                carry = 1
                new_val = new_val%10
            temp.next = ListNode(new_val)
            temp = temp.next
            curr1 = curr1.next

        while curr2:
            new_val = curr2.val + carry
            carry = 0
            if new_val > 9:
                carry = 1
                new_val = new_val%10
            temp.next = ListNode(new_val)
            temp = temp.next
            curr2 = curr2.next
                

        if carry == 1:
            temp.next = ListNode(carry)

        return head.next
                
