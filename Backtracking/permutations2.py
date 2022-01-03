class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        
        def permutation(nums,index,op):
            
            if index == len(nums):
                it = []
                for e in nums:
                    it.append(e)
                    
                if it not in op:
                    op.append(it)
                
                
            else:
                for j in range(index,len(nums)):
                    if j != index:
                        nums[j], nums[index] = nums[index], nums[j]
                        
                    permutation(nums,index+1,op)
                    
                    if index != j:
                        nums[index], nums[j] = nums[j], nums[index]
                        
                    
        op = []
        permutation(nums,0,op)
        return op
                    
                    
