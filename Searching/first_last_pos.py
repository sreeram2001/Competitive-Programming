class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        arr = [None]*2
        
        
        for i in range(len(nums)):
            if nums[i] == target and arr[0] == None:
                arr[0] = i
                
            if nums[i] == target:
                arr[1] = i
                
        
        if arr[0] == None:
            return [-1,-1]
        else:
            return arr
