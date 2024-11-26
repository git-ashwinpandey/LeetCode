def findChampion(self, n: int, edges: List[List[int]]) -> int:
        indegree = [0] * n
        for pair in edges:
            indegree[pair[1]] += 1
        
        min_score = min(indegree)
        min_count = indegree.count(min_score)
        
        if min_count > 1:
            return -1
        
        return indegree.index(min_score)