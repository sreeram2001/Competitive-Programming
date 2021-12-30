class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def bracket(arr,l,r):
            
            if len(arr) == 2*n:
                op.append("".join(arr))
                
                
            if l < n:
                arr.append("(")
                bracket(arr,l+1,r)
                arr.pop()
                
                
            if r < l:
                arr.append(")")
                bracket(arr,l,r+1)
                arr.pop()
                
                            
        op = []
        bracket([],0,0)
        return op
        
