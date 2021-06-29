

#Given a String e.g(ABZ) Find the distance or step taken to move from A to B to Z. ( Shortest ). Consider Z is right before A ( Circular Array )

s = 'AZGB'
res = 0
pos = 65

for i in s:
    val = abs(pos-ord(i))
    pos = ord(i)
    res = res + min(val,26-val)
print(res)
    

    
    
    

