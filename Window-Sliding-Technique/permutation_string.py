class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        l1 = len(s1)
        l2 = len(s2)
        
        freq_s1 = [0]*26
        window = [0]*26
        
        for i in s1:
            freq_s1[ord(i) - ord('a')] = freq_s1[ord(i) - ord('a')] + 1
            
        
        for ind in range(len(s2)-len(s1)+1):
            
            if ind==0:
                for ii in range(len(s1)):
                    window[ord(s2[ii]) - ord('a')] = window[ord(s2[ii]) - ord('a')] + 1  
                
            else:
                window[ord(s2[ind+len(s1)-1]) - ord('a')] = window[ord(s2[ind+len(s1)-1]) - ord('a')] + 1
            
  
            if freq_s1 == window:
                return True
            
            window[ord(s2[ind]) - ord('a')] = window[ord(s2[ind]) - ord('a')] - 1
            
            
        return False
            
