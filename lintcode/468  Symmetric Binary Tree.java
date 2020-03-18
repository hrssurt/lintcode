/****************************  TITLE  *****************************/
/*468  Symmetric Binary Tree.java*/



/****************************  DESCRIPTION  *****************************/
/*
Given a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
*/



/****************************  EXAMPLES  *****************************/
/*
Input: {1,2,2,3,4,4,3}
Output: true
Explanation:
         1
        / \
       2   2
      / \ / \
      3 4 4 3

is a symmetric binary tree.

*/



/****************************  CODE  *****************************/
/**
 * Definition of TreeNode:
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left, right;
 *     public TreeNode(int val) {
 *         this.val = val;
 *         this.left = this.right = null;
 *     }
 * }
 */

public class Solution {
    /**
     * @param root: the root of binary tree.
     * @return: true if it is a mirror of itself, or false.
     */
    public boolean isSymmetric(TreeNode root) {
        if (root == null) {
            return true;
        }
        return check(root.left, root.right);
    }
    
    
    public boolean check(TreeNode root1, TreeNode root2) {
        if (root1 == null && root2 == null) return true;
        if (root1 == null || root2 == null) return false;
        if (root1.val != root2.val) return false;
        
        return check(root1.left, root2.right) && check(root1.right, root2.left);
    }
}
