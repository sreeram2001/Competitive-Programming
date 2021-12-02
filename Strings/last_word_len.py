class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        ll = s.split(" ")
        
        for i in range(len(ll)-1,-1,-1):
            if ll[i] != '':
                return len(ll[i])
            
