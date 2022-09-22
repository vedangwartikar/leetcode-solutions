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
        while slow.next and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        if fast.next:
            slow = slow.next
                
        node = head
        while node:
            if node.next == slow:
                node.next = slow.next
            node = node.next
        
        return head
        