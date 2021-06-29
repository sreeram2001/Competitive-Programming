
#given the number of spins "n" determine the minimum no. of stops (i.e get the maximum number for each spin and sum it)

n = 4
spins = ['712','246','365','312']
arr = []
total_sum = 0

for i in spins:
    ele = list(map(int,i))
    arr.append(ele)


while n>-1:
    maximum = 0
    for i in arr:
        if len(i)==0:
            break
        else:
            print(i)
            i.sort()
         
            cur_max = i.pop()
            if cur_max >= maximum:
                maximum = cur_max
        
    n = n - 1 
    total_sum = total_sum + maximum
    
print(total_sum)



        
    
    
        
    
    
    
    
