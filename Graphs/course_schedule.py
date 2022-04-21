class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        visited = set()
        req = set()
        
        course_take = defaultdict(list)
        for i in prerequisites:
            course_take[i[0]].append(i[1])
            
        def bfs(node):
            for n in course_take[node]:
                if n in req:
                    return False
                
                if n not in visited:
                    req.add(n)
                    if bfs(n) == False:
                        return False
                    
                    visited.add(n)
                    req.remove(n)
            visited.add(node)
            
            
        for node in range(numCourses):
            if node not in visited:
                if bfs(node) == False:
                    return False
                
        return True
        
