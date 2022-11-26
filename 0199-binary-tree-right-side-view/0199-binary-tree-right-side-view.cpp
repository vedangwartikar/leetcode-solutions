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
    vector <int> right_view = {};
    int level = 0;
    vector<int> rightSideView(TreeNode* root) {
        recursive_right(root, level);
        recursive_right(root, 0);
        return right_view;
    }
    
    void recursive_right(TreeNode* root, int level) {
        if (!root) {
            return;
        }
        if (level == right_view.size()) {
            right_view.push_back(root->val);
        }
        recursive_right(root->right, level + 1);
        recursive_right(root->left, level + 1);
    }
};