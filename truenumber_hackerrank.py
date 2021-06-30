
#minimum number of iterations required make a number a true Number(which has even digits)

def true_number(n):
    num1 = n
    num2 = n
    flag = False
    count1 = 0
    count2 = 0
    
    #increment count
    while flag==False:
        val = list(map(int,str(num1)))
        
        for i in val:
            if i%2==0:
                flag = True
            else:
                flag = False
                break
       
        if flag==True:
            break
        else:
            num1 = num1 + 1
            count1 = count1 + 1

   
    #decrement count
    flag = False
    while flag == False:
        val = list(map(int, str(num2)))
        
        for i in val:
            if i%2==0:
                flag = True
            else:
                flag = False
                break
        
        if flag==True:
            break
        else:
            num2 = num2  - 1
            count2 = count2 + 1
            
            
    return min(count1,count2)
                
            
#driver code
n = 11
print("Total Iterations: ",true_number(n))