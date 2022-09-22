# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        """
        1 -> 2 -> 3 -> 4 -> 5 -> None
        Get the middle+1 of the linked list (4)
        Reverse the linked list from that point (5 -> 4 -> None)
        Reorder both the lists (first -> next = second; second.next = fnext; and so on)by traversing till the second list node is not None (5 -> 4 -> 3 -> 2 -> 1 -> None)
        """
        slow, fast = head, head
        while slow.next and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        slow = slow.next
            
        new = None
        while slow:
            next = slow.next
            slow.next = new
            new = slow
            slow = next
        
        rm = head
        while rm.next and rm.next.next:
            rm = rm.next

        rm.next = None
                
        first, second = head, new
        while second:
            fnext = first.next
            snext = second.next
            first.next = second
            second.next = fnext
            first = fnext
            second = snext