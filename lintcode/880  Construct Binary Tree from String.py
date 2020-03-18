"""***************************  TITLE  ****************************"""
"""880  Construct Binary Tree from String.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
You need to construct a binary tree from a string consisting of parenthesis and integers.
"""



"""***************************  EXAMPLES  ****************************"""
"""
'('
"""



"""***************************  CODE  ****************************"""
        stack = []
        for idx, char in enumerate(s):
            if char == "(":
                stack.append(char)
            elif char == ")":
                stack.pop(0)
                
            if not stack:
                return idx
        return None
                
        
    
    def str2tree(self, s):
        if not s:
            return None
        if '(' not in s:
            return TreeNode(int(s))
        else:
            first_bracket = s.index("(")
            root = TreeNode(s[:first_bracket])
            s = s[first_bracket:]
            matching_backet = self.find_next_matching_bracket_idx(s)
            root.left = self.str2tree(s[1:matching_backet])
            root.right = self.str2tree(s[matching_backet+2:-1])
            return root
            
        
