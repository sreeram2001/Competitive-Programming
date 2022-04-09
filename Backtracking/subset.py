class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def backtracking(curr,combi):
            if len(combi) == i:
                op.append(combi[:])
            
            for j in range(curr,l):
                combi.append(nums[j])
  
                backtracking(j+1,combi)
                
                combi.pop()
                
            
    
        l = len(nums)
        op = []
        for i in range(l+1):
            backtracking(0,[])
            
        return op
            
            
