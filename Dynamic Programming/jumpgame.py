class Solution:
    def canJump(self, nums: List[int]) -> bool:
        l = len(nums)
        
        if l==1:
            return True
        
        if nums[0] == 0:
            return False
        
        dp = [0]*len(nums)
        dp[0] = nums[0]
        
        for i in range(1,l):
            
            if dp[i-1] > 0:
                dp[i] = max(dp[i-1]-1,nums[i])
            
        if dp[l-2] > 0:
            return True
        return False
        
        
                
