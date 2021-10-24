#Coin Change - Leetcode - Dynamic Programming

def coins_sum(arr,target):
    
    r = len(arr) + 1
    c = target + 1
    
    dp = [[0 for i in range(c)]for j in range(r)]
    
    dp[0] = [100000]*len(dp[0])
    

    for i in range(1,r):
        for j in range(1,c):
            
            if arr[i-1] <= j:
                dp[i][j] = min(dp[i-1][j],1+dp[i][j-arr[i-1]])
                
            else:
                dp[i][j] = dp[i-1][j]
                
    print(dp)
    return dp[-1][-1]
            

#driver code
coins = [1,2,5]
amount = 9
ans = coins_sum(coins,amount)
print(ans)

