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
    int diameterOfBinaryTree(TreeNode* root) {
        int diameter = 0;											// initially diameter is 0
        helper(root, diameter);										// call recursive helper function
        return diameter;											// return the max diameter
    }
    
    int helper(TreeNode* root, int &diameter) {						// recursive helper function
        if (!root) {												// if root is not NULL
            return 0;												// return 0
        }
        int left_height = helper(root->left, diameter);				// get the left height
        int right_height = helper(root->right, diameter);			// get the right height
        diameter = max(diameter, left_height + right_height); 		// maintain the diameter here (diameter is basically left height + right height)
        
        return 1 + max(left_height, right_height);
    }
};