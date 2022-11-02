# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    count = 0
    kth_node = -1
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(root):
            if not root:
                return
            self.kthSmallest(root.left, k)
            self.count += 1
            if self.count == k:
                self.kth_node = root.val
                return
            self.kthSmallest(root.right, k)
        inorder(root)
        return self.kth_node