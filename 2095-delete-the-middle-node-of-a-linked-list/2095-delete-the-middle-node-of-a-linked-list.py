# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
Traverse using slow and fast pointers but also keep a reallyslow pointer that should be pointing at middle-1 (node before the slow)
Remove reallyslow's next (middle node) using next.next
O(n)
"""
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
        