class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        
        def binarysearch(nums,low,high,target,arr):
            
            if low > high :
                return -1
            
            mid = (low+high)//2
            
            if nums[mid] == target:
                arr.append(mid)
                binarysearch(nums,mid+1,high,target,arr)
                binarysearch(nums,0,mid-1,target,arr)
                
                
            elif nums[mid] < target:
                binarysearch(nums,mid+1,high,target,arr)
                
                
            else:
                binarysearch(nums,0,mid-1,target,arr)
               
            
            
        index = []
        binarysearch(nums,0,len(nums)-1,target,index)

        if len(index) == 0:
            index = [-1,-1]
        
        return [min(index),max(index)]
