# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        sum = [0]
        def recursive_inorder(root, low, high):
            if not root:
                return
            recursive_inorder(root.left, low, high)
            if low <= root.val <= high:
                sum[0] += root.val
            recursive_inorder(root.right, low, high)
        recursive_inorder(root, low, high)
        return sum[0]