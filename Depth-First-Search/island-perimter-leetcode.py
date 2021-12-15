class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        lr = len(grid)
        lc = len(grid[0])
        
        visited = set()
        island = []

        
        #dfs
        def check(r,c):
            if r >= lr or c >= lc or r < 0 or c < 0 or grid[r][c]==0:
                island.append(1)
                return
                
            elif (r,c) in visited:
                return 0
            
            
            visited.add((r,c))
                
            check(r-1,c)
            check(r+1,c)         
            check(r,c-1)
            check(r,c+1)
            
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
            
                    check(i,j)
                
                
        return sum(island)
                
