class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        visit_path = set()
        r = len(board)
        c = len(board[0])
        
        def backtrack(row,col,pos):
            if pos == len(word):
                return True
            
            if row<0 or col<0 or row>=r or col>=c or (word[pos] != board[row][col]) or ((row,col)in visit_path):
                return False
            
            visit_path.add((row,col))
            
            op = (backtrack(row+1,col,pos+1) or backtrack(row-1,col,pos+1) or
                 backtrack(row,col+1,pos+1) or backtrack(row,col-1,pos+1))
                
            visit_path.remove((row,col))
            return op
        
        for row in range(r):
            for col in range(c):
                if backtrack(row,col,0):
                    return True        
        
        return False
            
