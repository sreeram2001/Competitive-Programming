#Given nXn matrix print the matrix with maximum sum

def max_matrix(mat,k):
    
    lr = len(mat)
    lc = len(mat[0])
    maxi = -99999999
    
    for i in range(lr-k+1):
        for j in range(lc-k+1):
            
            sumi = 0
            for r in range(i,i+k):
                for c in range(j,j+k):
                    sumi = sumi + mat[r][c]
                    
            if sumi >= maxi:
                maxi = sumi
                
    return maxi

#driver-code
k = 3
matrix = [
[1, 1, 1, 1, 1],
[2, 2, 2, 2, 2],
[3, 3, 3, 3, 3],
[4, 4, 4, 4, 4],
[5, 5, 5, 5, 5]]

op = max_matrix(matrix,k)
print(op)
