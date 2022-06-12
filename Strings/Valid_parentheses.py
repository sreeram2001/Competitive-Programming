class Solution:
    def isValid(self, s: str) -> bool:
        
        if len(s) == 1:
            return False
        
        brackets = []
        
        for i in s:
            if not brackets:
                if i in [")","]","}"]:
                    brackets.append(i)
                    
            if i in ['(','{','[']:
                brackets.append(i)
                
            elif i==')':
                if brackets:
                    c = brackets.pop()
                    if c != '(':
                        return False
                    
            elif i==']':
                if brackets:
                    c = brackets.pop()
                    if c != '[':
                        return False
                    
            elif i=='}':
                if brackets:
                    c = brackets.pop()
                    if c != '{':
                        return False
            
        if brackets:
            return False
        else:
            return True
            
                         
