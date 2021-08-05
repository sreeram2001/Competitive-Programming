#Input
#First line of the input contains two space separated integers, R and C. It is followed by R lines, each line has C space separated integers. Each integer denotes the units of gold present in that particular cell.
#Next line has number Q, it is followed by Q queries each query in a single line. Each query is four space separated integers x1, y1, x2 and y2.

#Output
#For each query, you have to print a single number the total gold contained in that sub rectangle.

#Constraints 1 <= R <= 1000 1 <= C <= 1000 1 <= x1 <= x2 <= R 1 <= y1 <= y2 <= C


ip = input()
inp = list(map(int,ip.split()))
print(inp)

mat = []

#the 2d matrix
for i in range(inp[0]):
    inpu = input()
    row = list(map(int,inpu.split()))
    mat.append(row)
    
print(mat,"\n")


query = int(input("Query: "))

for i in range(query):
    rec_inp = input("Enter x1, y1, x2,y2 : ")
    rec_dim = list(map(int,rec_inp.split()))
    print("dimension: ",rec_dim)

    #summing all no.s
    sumi = 0
    for x in range(rec_dim[0]-1,rec_dim[2]):
        for y in range(rec_dim[1]-1,rec_dim[3]):
            sumi = sumi + mat[x][y]
        
    print("Sum: ",sumi,"\n")
