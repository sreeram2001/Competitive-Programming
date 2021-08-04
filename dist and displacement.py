
n = int(input())
c = 'R'
dist = 10
side = 0
straight = 0


for i in range(n):
    
    if c=='R':
        side = side + dist
        dist = dist + 10
        c = "U"
        
    elif c=="U":
        
        straight = straight + 10
        c = "L"
        dist = dist + 10
        
    elif c=="L":
        
        side = side - dist
        c = "D"
        dist = dist + 10
        
    elif c=='D':
        
        straight = straight - dist
        c='A'
        dist = dist + 10
        
        
    elif c=='A':
        side = side + dist
        c = 'R'
        dist = dist + 10
        
        
print("total distance covered: ",side)
print("displacement :",straight)
