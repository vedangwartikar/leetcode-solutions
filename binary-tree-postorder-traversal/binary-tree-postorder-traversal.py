# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        stack1, stack2 = [], []
        stack1.append(root)
        while len(stack1):
            node_add = stack1.pop(-1)
            if node_add.left:
                stack1.append(node_add.left)
            if node_add.right:
                stack1.append(node_add.right)
            stack2.append(node_add.val)
        return stack2[::-1]