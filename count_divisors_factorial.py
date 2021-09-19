
ip = int(input())

count = 1
multi  = 1

while count <= ip:
    multi = multi*(count)
    count = count + 1
    
factorial = multi
factors = []

for i in range(1,factorial+1):
    if factorial%i == 0:
        factors.append(i)
 
print(factors)       
print(len(factors))
    
    