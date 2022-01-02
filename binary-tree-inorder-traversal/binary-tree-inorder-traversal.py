# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack, inorder = [], []
        current_node = root
        while True:
            if current_node:
                stack.append(current_node)
                current_node = current_node.left
            else:
                if not len(stack):
                    break
                current_node = stack.pop(-1)
                inorder.append(current_node.val)
                current_node = current_node.right
        return inorder