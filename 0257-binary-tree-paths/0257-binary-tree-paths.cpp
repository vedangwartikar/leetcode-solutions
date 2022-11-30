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
        if (root == NULL) { // if no root
            return {}; // return no paths
        }
        vector<string> paths; // paths
        path(root, "", paths); // define a helper function that can be called recursively
        return paths; // return the paths
    }
    
    void path(TreeNode* root, string current_path, vector<string> &paths) { // recursive helper function
        current_path += to_string(root->val); // add the current root's value
        
        if (root->left != NULL) { // if root has a left
            path(root->left, current_path + "->", paths); // recursively call left subtree to add the value in the future
        }
        if (root->right != NULL) { // if root has a right
            path(root->right, current_path + "->", paths); // recursively call left subtree to add the value in the future
        }
        if (root->left == NULL && root->right == NULL) { // if a leaf node
            paths.push_back(current_path); // add the current computed path string to the result
        }
    }
};