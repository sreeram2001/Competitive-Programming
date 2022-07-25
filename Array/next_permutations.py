class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return nums
        
        #find first decreasing form behing, swap with just larger than that number ,              reverse the rest after swapped index
        
        i = len(nums)-2     #starting from last second index
        
        
        #finding first decreasing element thru reverse traversal
        while i>=0 and nums[i+1] <= nums[i]:
            i -= 1
            
        #swap with number just larger than that
        if i >= 0:
            j = len(nums)-1     #swapping from last index
            
            while nums[i] >= nums[j]:
                j = j - 1
                
            nums[i], nums[j] = nums[j], nums[i]
            
        #reverse the rest of the numbers which is after swapped index
        start = i+1
        end = len(nums)-1
        
        while start<end:
            nums[start], nums[end] = nums[end], nums[start]
            start = start + 1
            end = end - 1
        
        return nums
            
            
            
