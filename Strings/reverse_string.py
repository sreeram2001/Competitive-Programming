s = ["H","a","n","n","a"]

l = len(s)

        
if len(s)%2==0:
    mid = l//2
    
    for i in range(mid):
        s[i], s[l-i-1] = s[l-i-1], s[i]
        print(i,l-i-1)
        

elif len(s)%2 == 1:
    mid = l//2
    
    for i in range(mid):
        s[i], s[l-i-1] = s[l-i-1], s[i]
   
   
print(s)
