# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        retnode = dummy
        carry = 0
        while l1 or l2:
            if not l1:
                addition = l2.val
            elif not l2:
                addition = l1.val
            else:
                addition = l1.val + l2.val
            if carry:
                addition += carry
            if addition < 9:
                dummy.next = ListNode(addition)
                dummy = dummy.next
                carry = 0
            else:
                carry = addition // 10
                dummy.next = ListNode(addition%10)
                dummy = dummy.next
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2
        if carry:
            dummy.next = ListNode(carry)
        return retnode.next