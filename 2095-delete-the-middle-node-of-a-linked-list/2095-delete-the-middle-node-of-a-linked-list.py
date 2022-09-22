# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None
        slow, fast = head, head
        reallyslow = head
        
        while slow.next and fast.next and fast.next.next:
            reallyslow = slow
            slow = slow.next
            fast = fast.next.next
        if fast.next:
            reallyslow = slow
            slow = slow.next
        
        reallyslow.next = reallyslow.next.next
        
        return head
        