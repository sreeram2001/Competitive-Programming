

s = 'AZGB'
res = 0
pos = 65

for i in s:
    val = abs(pos-ord(i))
    pos = ord(i)
    res = res + min(val,26-val)
print(res)
    

    
    
    

