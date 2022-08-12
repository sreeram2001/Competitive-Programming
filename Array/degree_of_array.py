class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        
        min_l = float("inf")        #minimum length possible
        maxi_freq = 0
        
        dict = {}
        
        for i in nums:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] += 1
                
        maxi_freq = max(dict.values()) #max-key
        min_l = len(nums)
        
        index = {}
        #fixing index for first and last occurence
        for i in range(len(nums)):
            if dict[nums[i]] == maxi_freq:
                if nums[i] not in index:
                    index[nums[i]] = [i,i]
                else:
                    index[nums[i]][1] = i
                    
                    
        #find minimum length needed
        for i in index:
            min_l = min(min_l,index[i][1] - index[i][0])
        
        return min_l+1
