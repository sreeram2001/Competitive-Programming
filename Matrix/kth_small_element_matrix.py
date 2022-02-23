class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        l = matrix[0][0]
        h = matrix[-1][-1]
        n = len(matrix)
        
        def bs_counter(middle):
            r = 0
            c = n-1
            count = 0
            
            for r in range(n):
                while matrix[r][c] > middle and c >= 0:
                    c = c - 1
                count = count + c + 1
            return count
        
        
        while l < h:
            mid = (l+h)//2
            
            if bs_counter(mid) < k:
                l = mid + 1
            else:
                h = mid
                
        return l
            
