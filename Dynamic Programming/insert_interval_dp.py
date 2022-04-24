class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        op = []
        intervals.append(newInterval)
        intervals.sort()
        
        prev = intervals[0]
        
        for i in range(1,len(intervals)):
            
            if intervals[i][0] <= prev[1]:
                prev[1] = max(prev[1],intervals[i][1])
                
            else:
                op.append(prev)
                prev = intervals[i]
                
        op.append(prev)
        return op
                
