"""***************************  TITLE  ****************************"""
"""7  Serialize and Deserialize Binary Tree.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Design an algorithm and write code to serialize and deserialize a binary tree. Writing the tree to a file is called 'serialization' and reading back from the file to reconstruct the exact same binary tree is 'deserialization'.
"""



"""***************************  EXAMPLES  ****************************"""
"""
serialize
"""



"""***************************  CODE  ****************************"""
class Solution:
    def serialize(self, root):
        q = [root]
        result = []
        while q:
            head = q.pop(0)
            if head:
                val, left, right = head.val, head.left, head.right
                q.append(left)
                q.append(right)
                result.append(str(val))
            else:
                result.append('None')
        return " ".join(result)
        
        
    
    def deserialize(self, data):
        data = [TreeNode(val) if val != 'None' else None for val in data.split(" ")]
        slow, fast = 0, 1
        while slow < len(data):
            if data[slow]:
                if fast < len(data):
                    data[slow].left = data[fast]
                if fast + 1 < len(data):
                    data[slow].right = data[fast+1]
                fast += 2
                slow += 1
            else:
                slow += 1
            
        return data[0]

