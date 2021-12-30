# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        stack, ans = [], []
        stack.append(root)
        while len(stack):
            top_node = stack.pop(-1)
            ans.append(top_node.val)
            if top_node.right:
                stack.append(top_node.right)
            if top_node.left:
                stack.append(top_node.left)
        return ans