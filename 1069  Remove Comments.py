"""***************************  TITLE  ****************************"""
"""1069  Remove Comments.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Given a C++ program, remove comments from it. The program source is an array where source[i] is the i-th line of the source code. This represents the result of splitting the original source code string by the newline character \n.
"""



"""***************************  EXAMPLES  ****************************"""
"""
source[i]
"""



"""***************************  CODE  ****************************"""
    def removeComments(self, source):
        result, buffer, commenting = [], "", False
        for line in source:
            idx = 0
            while idx < len(line):
                char = line[idx]
                if char == '/' and idx + 1 < len(line) and line[idx+1] == "/" and not commenting:
                    break
                elif char == '/' and idx + 1 < len(line) and line[idx+1] == "*" and not commenting:
                    commenting = True
                    idx += 1
                elif char == '*' and idx + 1 < len(line) and line[idx+1] == "/" and commenting:
                    commenting = False
                    idx += 1
                elif commenting:        # all the condition
                    idx += 1
                    continue
                else:
                    buffer += char
                idx += 1
            
            if not commenting and buffer:
                result.append(buffer)
                buffer = ""
        
        return result
                    
            
