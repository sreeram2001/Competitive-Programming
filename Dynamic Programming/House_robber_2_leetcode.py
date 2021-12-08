class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return max(nums)
        

        def house_rob(arr):
            
            dp = [None for i in range(len(arr))]
        
            dp[0] = arr[0]
            dp[1] = max(arr[0],arr[1])
            
            for i in range(2,len(arr)):
                dp[i] = max(dp[i-1],arr[i] + dp[i-2])
                
            
            return dp[-1]
        
        
        max_amount = max(house_rob(nums[:-1]),house_rob(nums[1:]))
        return max_amount
        
