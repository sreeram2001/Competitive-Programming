class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        row = len(grid)
        col = len(grid[0])
        num = 0
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    
                    num = num + 1
                    q = [(i,j)]
                    
                    while q:
                        r,c = q.pop()
                        
                        if((0 <= r <row) and (0 <= c <col) and (grid[r][c] == '1')):
                            grid[r][c] = '0'

                            
                            for dir in directions:
                                q.append((r+dir[0],c+dir[1]))
                                
                                
        return num
