class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        lr = len(image)
        lc = len(image[0])
        
        oldcolor = image[sr][sc]
        
        if oldcolor == newColor:
            return image                                #if both colors are same, no change
        
        
        def modify(image,r,c,newColor):
            
            if image[r][c] == oldcolor:
                image[r][c] = newColor
                
                if r >= 1:
                    modify(image,r-1,c,newColor)
                
                if c >= 1:
                    modify(image,r,c-1,newColor)
                
                if r+1 < lr:
                    modify(image,r+1,c,newColor)
                
                if c+1 < lc:
                    modify(image,r,c+1,newColor)

            
        modify(image,sr,sc,newColor)
        return image
        
