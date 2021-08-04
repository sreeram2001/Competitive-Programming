import itertools

a = int(input())
b = int(input())

lst = ["".join(i) for i in itertools.permutations(str(a))]
num_lst = list(map(int,lst))

mini = 1000000000000         #minimum of all

for i in num_lst:
    if i > b:
        if  i <= mini:
            mini = i
            
if mini == 1000000000000:
    print(-1)
else:
    print("The Number Is: ",mini)
        
        