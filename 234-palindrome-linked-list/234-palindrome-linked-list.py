# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast, prev = head, head, head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None
        new = None
        while slow:
            next = slow.next
            slow.next = new
            new = slow
            slow = next
        while new and head:
            if new.val != head.val:
                return False
            new = new.next
            head = head.next
        return True
            