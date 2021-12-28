# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import sys

class Solution:
    
    def isBST (self, root, low, high):
        if root == None:
            return True
        if root.val >= high or root.val <= low:
            return False
        return self.isBST (root.left, low, root.val) and self.isBST (root.right, root.val, high)
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isBST (root, -sys.maxsize, sys.maxsize)