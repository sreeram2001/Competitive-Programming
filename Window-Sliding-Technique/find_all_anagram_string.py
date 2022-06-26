class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        index = []
        left = right = 0
        
        if len(s) < len(p):
            return index
        
        hash_p = [0 for i in range(26)]
        hash_s = [0 for i in range(26)]
        
        for i in p:
            hash_p[ord(i) - 97] = hash_p[ord(i) -97] + 1
        
        for i in range(len(p)):
            ind = ord(s[i]) - 97
            hash_s[ind] = hash_s[ind] + 1
            
        if hash_s == hash_p:
            index.append(0)

        right = len(p)-1
        #sliding starts here
        for i in range(len(p),len(s)):
            
            hash_s[ord(s[left])-97] -= 1
            
            left = left + 1
            right = right + 1
            
            hash_s[ord(s[right])-97] += 1
            
            if hash_s == hash_p:
                index.append(left)
        
        return index

            
            
