class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        lr = len(grid)
        lc = len(grid[0])
        visited = set()
        maxi = 0
        
        
        def islands(r,c,curr):
            if (r,c) not in visited and grid[r][c] == 1:
                curr = curr + 1
                visited.add((r,c))
            
                if r >= 1:
                    curr = islands(r-1,c,curr)
                
                if c >= 1:
                    curr = islands(r,c-1,curr)
                
                if r+1 < lr:
                    curr = islands(r+1,c,curr)
                
                if c+1 < lc:
                    curr = islands(r,c+1,curr)
            
            return curr
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                count = 0
                
                if (i,j) not in visited and grid[i][j] == 1 :
                    count = islands(i,j,count)
                    if maxi <= count:
                        maxi = count
     
        return maxi
