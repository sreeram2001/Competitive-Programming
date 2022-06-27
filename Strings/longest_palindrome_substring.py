class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        string = ""
        op = 0
        
        for i in range(len(s)):
            
            #odd-length palindromes
            l = r = i                #left side pointer and right side pointers
        
            #using while loop to iterate from middle to both ends and check if palindrome
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if op < (r-l+1):
                    string = s[l:r+1]
                    op = r-l+1
                
                l = l - 1
                r = r + 1
             
            
            #even-length palindromes
            l = i
            r = i + 1
            
            while l>=0 and r<len(s) and s[l]==s[r]:
                if op < (r-l+1):
                    string = s[l:r+1]
                    op = r-l+1
                    
                l = l - 1
                r = r + 1
                
        return string
