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
    vector<vector<int>> levelOrder(TreeNode* root) {
        if (root == NULL) {
            return {};
        }
        vector <vector <int>> result;
        deque <TreeNode*> queue;
        queue.push_back(root);
        while (queue.size() > 0) {
            vector <int> level = {};
            int queue_size = queue.size();
            for (int i = 0; i < queue_size; i++) {
                TreeNode* queue_front = queue.front();
                level.push_back(queue_front->val);
                queue.pop_front();
                if (queue_front->left != NULL) {
                    queue.push_back(queue_front->left);
                }
                if (queue_front->right != NULL) {
                    queue.push_back(queue_front->right);
                }
            }
            result.push_back(level);
        }
        return result;
    }
};