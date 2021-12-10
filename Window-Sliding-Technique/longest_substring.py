class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == None:
            return 0
        
        length = 0
        substring = ""
        
        for ele in s:
            if ele not in substring:
                substring = substring +  ele
            
            elif ele in substring:
                i = substring.index(ele)
                substring = substring[i+1:] + ele
                
            length = max(length,len(substring))
            
            
        return length
