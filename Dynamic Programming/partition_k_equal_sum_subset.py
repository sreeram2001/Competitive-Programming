class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:

        dp = [0]*k
        t = sum(nums)/k
        l = len(nums)
        nums.sort()
        nums = nums[::-1]
        
        def backtrack(ind):
            
            if ind == l:
                if len(set(dp))==1:
                    return True
                return False
            
            for i in range(k):
                dp[i] = dp[i] + nums[ind]
                
                if dp[i] <= t and backtrack(ind+1):
                    return True
                dp[i] = dp[i] - nums[ind]
                
                if dp[i]==0:
                    break
            return False
        
        return backtrack(0)
                
            
            
