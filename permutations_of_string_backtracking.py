
#print all permutations of a string - Backtracking Algorithm

def permutations(s,curr):
    
    if curr==len(s)-1:
        print("".join(s))
        
    for i in range(curr,len(s)):
        s[i], s[curr] = s[curr], s[i]
        permutations(s,curr+1)
        s[i], s[curr] = s[curr], s[i]
 

        
        
        

#driver code
s = 'ABC'
permutations(list(s),0)