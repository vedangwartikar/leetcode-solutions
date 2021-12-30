# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue  = []
        ans = []
        queue.append(root)
        while len(queue):
            level = []
            for i in range(len(queue)):
                queue_front = queue.pop(0)
                level.append(queue_front.val)
                if queue_front.left:
                    queue.append(queue_front.left)
                if queue_front.right:
                    queue.append(queue_front.right)
            ans.append(level)
        return ans
            