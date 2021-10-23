#dynamic Programming - Longest Subsequence 
#dp = [[0]] - Initialise zero in dp table

a = 'abcabcd'
b = 'abcd'

m = len(a)
n = len(b)

arr = [[0]*(n+1)]*(m+1)                 #Initialise dp-table with 0
print(arr)                              #empty array - dp table


#dp-table
for i in range(1,m+1):
    for j in range(1,n+1):

        if a[i-1] == b[j-1]:
            arr[i][j] = 1 + arr[i-1][j-1]
        else:
            arr[i][j] = max(arr[i-1][j],arr[i][j-1])
            
       
print(arr)            #dp-table
print(arr[m][n])
        
        
        





