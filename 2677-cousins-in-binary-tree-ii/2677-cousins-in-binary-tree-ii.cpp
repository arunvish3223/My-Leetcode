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
    TreeNode* replaceValueInTree(TreeNode* root) {
        if (!root) {
            return nullptr;
        }
        queue<TreeNode*> q;
        q.push(root);
        vector<int> levelSums;
        while (!q.empty()) {
            int size = q.size();
            int levelSum = 0;
            for (int i = 0; i < size; ++i) {
                TreeNode* node = q.front();
                q.pop();
                levelSum += node->val;
                if (node->left) {
                    q.push(node->left);
                }
                if (node->right) {
                    q.push(node->right);
                }
            }
            levelSums.push_back(levelSum);
        }
        root->val = 0;
        q.push(root);
        int level = 1;
        while (!q.empty()) {
            int size = q.size();
            for (int i = 0; i < size; ++i) {
                TreeNode* node = q.front();
                q.pop();
                int sumChildren = 0;
                if (node->left) {
                    sumChildren += node->left->val;
                }
                if (node->right) {
                    sumChildren += node->right->val;
                }
                if (node->left) {
                    node->left->val = levelSums[level] - sumChildren;
                    q.push(node->left);
                }
                if (node->right) {
                    node->right->val = levelSums[level] - sumChildren;
                    q.push(node->right);
                }
            }
            level++;
        }
        return root;
    }
};