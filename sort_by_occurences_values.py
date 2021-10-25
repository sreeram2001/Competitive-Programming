""" Given an Array of n items, sort the array in ascending order, 
first by the number of items then by the values themselves
Example : arr[4,5,6,5,4,3] , output = [3,6,4,4,5,5]"""

item = [4,5,6,5,4,3]
item.sort()             #sort the array by values initially

l = len(item)
dict = {}
result = []

for i in range(l):
    if item[i] not in dict:
        dict[item[i]] = 1
    else:
        dict[item[i]] = 1 + dict[item[i]]

dict_sort = sorted(dict, key = lambda x:dict[x])
for i in dict_sort:
    count = dict[i]
    for j in range(count):
        result.append(i)
        
print("before sorting : ",item)
print("after sorting : ",result)
