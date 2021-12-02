strs = ["a","a","b"]
common = strs[0]

if len(strs) == 1:
    print(strs[0])
 
else:
  for i in range(1,len(strs)):
      res = ""
    
      ii = 0
      jj = 0
    
      while ii<len(common) and jj<len(strs[i]):
          if common[ii] != strs[i][jj]:
              break
        
          res = res + common[ii]
          ii = ii + 1
          jj = jj + 1
        
    
      common = res
    
  print(common)
