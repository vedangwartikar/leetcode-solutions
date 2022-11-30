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
    vector<string> binaryTreePaths(TreeNode* root) {
        if (root == NULL) {
            return {};
        }
        vector<string> paths;
        path(root, "", paths);
        return paths;    
    }
    
    void path(TreeNode* root, string current_path, vector<string> &paths) {
        current_path += to_string(root->val);
        if (root->left != NULL) {
            path(root->left, current_path + "->", paths);
        }
        if (root->right != NULL) {
            path(root->right, current_path + "->", paths);
        }
        if (root->left == NULL && root->right == NULL) {
            paths.push_back(current_path);
        }
    }
};