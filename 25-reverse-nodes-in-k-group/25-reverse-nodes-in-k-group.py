# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        curr = prev = after =  dummy
        
        count = 0
        while curr.next:
            curr = curr.next
            count += 1
        
        while count >= k:
            curr = prev.next
            after = curr.next 
            for i in range(1,k,1):
                curr.next = after.next
                after.next = prev.next
                prev.next = after
                after = curr.next
            prev = curr
            count -= k
        
        return dummy.next