class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        
        #we will use window sliding technique
        
        k = nums.count(1)   #find no. of 1's
        nums = nums + nums
        
        start = 0
        window = 0      #window to find ones
        op = 0          #to get max 1's grouped together
        
        for r in range(len(nums)):
            window = window + nums[r]
            
            #when length croses window size
            if r >= k:
                window = window - nums[start]   #remove element from left
                start = start + 1
                
            op = max(op,window)
            
        return k - op
                

        
        
  
        
