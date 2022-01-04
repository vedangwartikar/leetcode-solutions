# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        level = 0
        stack = []
        def recursive_rightview(root, level):
            if not root:
                return
            if level == len(stack):
                stack.append(root.val)
            recursive_rightview(root.right, level + 1)
            recursive_rightview(root.left, level + 1)
        recursive_rightview(root, 0)
        return stack