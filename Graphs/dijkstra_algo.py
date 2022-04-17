
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        edge = defaultdict(list)
        visited = set()
        op = 0
        
        for i in times:
            edge[i[0]].append((i[1],i[2]))
        
        q = [(0,k)]      #vertex, weight
        
        #bfs
        while q:
            weight, dest = heapq.heappop(q)
            
            if dest in visited:
                continue
                
            visited.add(dest)
            op = max(op,weight)
            
            for dest1, weight1 in edge[dest]:
                if dest1 not in visited:
                    heapq.heappush(q,(weight+weight1,dest1))
                    
        
        if len(visited) == n:
            return op
        else:
            return -1
            
