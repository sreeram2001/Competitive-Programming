class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        dp = [0 for i in range(len(s)+1)]
        dp[0] = True
        
        for i in range(len(s)):
            word = ""
            
            for j in range(i,len(s)):
                
                word = word + s[j]
                
                if word in wordDict:
                   
                    if dp[i]:
                        dp[j+1] = False
                        
        return dp[-1]
