class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        
        def permutation(nums,index,op):
            
            if index == len(nums):
                item = []
                
                for ele in nums:
                    item.append(ele)
                op.append(item)
                
                
            else:
                for j in range(index,len(nums)):
                    if j != index:
                        nums[j], nums[index] = nums[index], nums[j]
                        
                    permutation(nums,index+1,op)
                    
                    if j != index:
                        nums[j], nums[index] = nums[index], nums[j]
                        
         
        op = []
        permutation(nums,0,op)
        return op
            
