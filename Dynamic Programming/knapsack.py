
#Knapsack 

value = [20, 5, 10, 40, 15, 25]
weight = [1, 2, 3, 8, 7, 4]
w = 10
l = len(value)
dp = [[0 for i in range(w+1)] for j in range(l+1)]

for i in range(1,l+1):
    for j in range(w+1):
        
        if j >= weight[i-1]:
            dp[i][j] = max(dp[i-1][j], value[i-1] + dp[i-1][j-weight[i-1]])
        else:
            dp[i][j] = dp[i-1][j]
            
print(dp[-1][-1])
