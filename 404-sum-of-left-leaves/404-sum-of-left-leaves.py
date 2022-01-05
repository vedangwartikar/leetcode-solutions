# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        total = [0]
        left_flag = [False]
        def recursive_left(root):
            if not root:
                return
            if not root.left and not root.right and left_flag[0]:
                total[0] += root.val
            left_flag[0]= True
            recursive_left(root.left)
            left_flag[0]= False
            recursive_left(root.right)
        recursive_left(root)
        return total[0]