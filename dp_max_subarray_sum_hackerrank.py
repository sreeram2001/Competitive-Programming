
#Hackerrank - Max Array Sum - DP
#Given an array of integers, find the subset of non-adjacent elements with the maximum sum.
#Calculate the sum of that subset. 
#It is possible that the maximum sum is 0, the case when all elements are negative.

def maxsubsum(arr):
    l = len(arr)
    dp = [0]*l
    
    for i in range(l):
        
        if i==0:
            dp[i] = arr[0]
            
        elif i==1:
            dp[i] = max(arr[0],arr[1])
            
        else:
            dp[i] = max(arr[i],arr[i]+dp[i-2],dp[i-1])
            
            
    return dp[l-1]
    
    
#driver-code
a = [-2,1,3,-4,5]
print(maxsubsum(a))