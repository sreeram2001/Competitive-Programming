
arr = [-1,1,0,-3,3]
answer = []

if len(arr)==2:
    arr = arr[::-1]
    print(arr)

for i in range(len(arr)):
    if i==0:
        a = arr[1]
        
        for j in range(2,len(arr)):
            a = a*arr[j]
        answer.append(a)
            
    else:
        a = arr[0]
        for j in range(1,len(arr)):
            if j != i:
                a = a*arr[j]
        answer.append(a)
        
print(answer)