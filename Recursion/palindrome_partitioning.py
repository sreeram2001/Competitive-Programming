class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        if len(s) == 0:
            return [[]]
        
        def palindrome(op,arr,s):
            
            if len(s)==0:
                op.append(arr)
                return
                
            for i in range(1,len(s)+1):
                if s[:i] == s[:i][::-1]:
                    palindrome(op,arr+[s[:i]],s[i:])
                
        op = []
        palindrome(op,[],s)
        return op
            
