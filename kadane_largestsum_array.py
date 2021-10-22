
#kadane algorithm to find largest sum contagious
a = [2,-2,2,5]
n = len(a)

maxi = a[0]
curr_maxi = 0

start = 0
end = 0
s = 0

for i in range(n):
    curr_maxi = curr_maxi + a[i]        #sum iteratively
    
    if curr_maxi >= maxi:
        maxi = curr_maxi                #update max only if sum exceeds max
        start = s                       #update starting position
        end = i                         #update end pos
        

    if curr_maxi < 0:                   #if sum is -ve, initialise again to 0
        curr_maxi = 0
        s = i + 1
        
print(maxi)
print(start,end)

