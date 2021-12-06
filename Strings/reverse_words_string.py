class Solution:
    def reverseWords(self, s: str) -> str:
        string = s.split(" ")
        
        for i in range(len(string)):
            string[i] = string[i][::-1]
            
        return " ".join(string)
