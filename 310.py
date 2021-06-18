# https://leetcode.com/problems/minimum-height-trees/

INF = 0x3f3f3f3f

class Solution:

    # Traverse via bfs
    def traverse(self, edges: List[List[int]], start: int) -> List[int]:
        n = len(edges)+1 # number of nodes

        # Convert the list of edges into a adjacency list
        adjacency_list = [[] for _ in range(n)]
        for u, v in edges:
            adjacency_list[u].append(v)
            adjacency_list[v].append(u)

        distances = [INF for _ in range(n)]
        
        distances[start] = 0
        queue = [start]
        while len(queue) > 0:
            s = queue.pop(0)
            for t in adjacency_list[s]:
                if distances[t] != INF: continue
                distances[t] = distances[s] + 1
                queue.append(t)                
        
        return distances
        
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        distances = self.traverse(edges, 0)
        max_distance = max(distances)
        
        s = distances.index(max_distance)
        distances_s = self.traverse(edges, s)
        max_distance_s = max(distances_s)
        
        t = distances_s.index(max_distance_s)
        distances_t = self.traverse(edges, t)
        max_distance_t = max(distances_t)
        
        assert max_distance_s == max_distance_t
        
        if max_distance_s % 2 == 0:
            candidates = [max_distance_s//2]
        else:
            candidates = [(max_distance_s-1)//2, (max_distance_s+1)//2]
        
        answer = []
        for i in range(n):
            if distances_s[i] not in candidates: continue
            if distances_t[i] not in candidates: continue
            answer.append(i)
        return answer
        
# From leetcode
# n = 10
# edges = [[0,3],[1,3],[2,3],[4,3],[5,3],[4,6],[4,7],[5,8],[5,9]]

# From leetcode
# n = 5
# edges = [[0,1],[0,2],[0,3],[3,4]]