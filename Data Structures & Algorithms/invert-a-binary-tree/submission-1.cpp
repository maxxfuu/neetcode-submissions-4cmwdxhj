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
    TreeNode* invertTree(TreeNode* root) {
        // base case 1: if node left and right is nullptr then its a leaf node. 
        if (!root) {
            return nullptr; 
        }

        //base case 2: if 
        if (root->left == nullptr and root->right == nullptr) {
            return root; 
        } else {
            TreeNode* temp = root->left;
            root->left = root->right;
            root->right = temp; 
        }
            invertTree(root->right);
            invertTree(root->left); 
        return root; 
  
    }
};
