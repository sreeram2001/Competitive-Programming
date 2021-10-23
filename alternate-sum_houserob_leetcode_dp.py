#House Robber Leetcode using Dynamic Programming

def dp_house(nums,l):
    
    if l == 1:
        return nums[0]
        
    if l == 2:
        return max(nums[0],nums[1])
        
        
    nums[1] = max(nums[0],nums[1]) 
    for i in range(2,l):
        nums[i] = max(nums[i-1],nums[i]+nums[i-2])
        
    return nums[l-1]
        
#driver code
arr = [2,7,9,3,1]
l = len(arr)
print(dp_house(arr,l))
