def sub_matrix_one(m):
    lr = len(m)
    lc = len(m[0])
    maxi = -1
    
    dp = [[0 for i in range(lc)]for j in range(lr)]
    
    for i in range(1,lr):
        for j in range(1,lc):
            if m[i][j] == 1:
                dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1]) + 1
            else:
                dp[i][j] = 0
                
            if dp[i][j] >= maxi:
                maxi = dp[i][j]
                
    return str(maxi)+'X'+str(maxi)

#driver-code
matrix = [[0, 1, 1, 0, 1],
    [1, 1, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0]]
    
print("Maximum Size of Array With 1's : ",sub_matrix_one(matrix))