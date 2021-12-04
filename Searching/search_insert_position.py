class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        low = 0
        high = len(nums)-1
        
        if nums[low] >= target:
            return low

        
        while low < high:
            mid = (low+high)//2
            
            if nums[mid] == target:
                return mid
            
            elif nums[mid] < target:
                low = mid+1
                
            else:
                high = mid-1
                
        
        if target < nums[low]:
            return low
        
        elif target > nums[high]:
            return high+1
        
        else:
            return high
        
