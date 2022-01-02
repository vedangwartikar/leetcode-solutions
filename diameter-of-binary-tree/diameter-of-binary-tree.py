# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def height(self, node, diameter):
        if not node:
            return 0
        left_height = self.height(node.left, diameter)
        right_height = self.height(node.right, diameter)
        diameter[0] = max(diameter[0], left_height + right_height)
        return 1 + max(left_height, right_height)
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = [0]
        self.height(root, diameter)
        return diameter[0]