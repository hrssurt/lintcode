"""***************************  TITLE  ****************************"""
"""470  Tweaked Identical Binary Tree.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Check two given binary trees are identical or not. Assuming any number of tweaks are allowed. A tweak is defined as a swap of the children of one node in the tree.
"""



"""***************************  EXAMPLES  ****************************"""
"""
Input:{1,2,3,4},{1,3,2,#,#,#,4}
Output:true
Explanation:
        1             1
       / \           / \
      2   3   and   3   2
     /                   \
    4                     4

are identical.

"""



"""***************************  CODE  ****************************"""
class Solution:
    def isTweakedIdentical(self, a, b):
        if not a and not b:
            return True
        if a and b and a.val == b.val:
            return self.isTweakedIdentical(a.left, b.left) and self.isTweakedIdentical(a                .right, b.right) or \
                self.isTweakedIdentical(a.left, b.right) and self.isTweakedIdentical(a                    .right, b.left)
        return False

