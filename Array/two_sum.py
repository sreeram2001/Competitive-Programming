class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        arr = []
        diff = 0
        
        for i in range(len(numbers)):
            diff = target - numbers[i]
            
            if diff in arr:
                return [arr.index(diff)+1,i+1]
            
            arr.append(numbers[i])
                    
                    
