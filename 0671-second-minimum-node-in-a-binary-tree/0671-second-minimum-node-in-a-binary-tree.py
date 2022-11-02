# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    mini, second_mini = float('inf'), float('inf')
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            if root.val <= self.mini:
                self.second_mini = self.mini if self.mini != root.val else self.second_mini
                self.mini = root.val
            else:
                self.second_mini = min(self.second_mini, root.val)
            # self.mini = min(self.mini, root.val)
            # self.second_mini = min(self.second_mini, root.val) if min(self.second_mini, root.val) != self.mini else self.second_mini
            # print(self.mini, self.second_mini)
            inorder(root.right)
        inorder(root)
        return self.second_mini if self.second_mini != float('inf') else -1