class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        #initialize the dp array
        dp = [1]*len(nums)
        
        
        #compare from element 0 until current element
        #check if its lesser than the current elements
        for i in range(1,len(nums)):
            for j in range(0,i):
                
                #nums[i] is the current element here
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i],1+dp[j])      #update value if condition is true
                    
        return max(dp)
