/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int maxDepth(TreeNode* root) {
        if (!root) {
            return 0; // incase root is NULL
        }
        int left_height = maxDepth(root->left); // go till leftmost root
        int right_height = maxDepth(root->right); // go till rightmost root
        return 1 + max(left_height, right_height); // add 1 each time we go one level up while returning
    }
};