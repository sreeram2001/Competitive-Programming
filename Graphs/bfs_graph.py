
class Solution:
    
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V, adj):
        
        op = []
        visit = [0 for i in range(V)]
        q = []
        
        q.append(0)
        visit[0] = 1
        
        while q:
            curr = q.pop(0)
            op.append(curr)
            
            for e in adj[curr]:
                if visit[e] == 0:
                    q.append(e)
                    visit[e] = 1
                    
        return op
                
