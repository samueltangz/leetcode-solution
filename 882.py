from heapq import heappush, heappop

INF = 2**100

class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        # Converts the edge list into an adjacency list
        adjacency_list = [[] for _ in range(n)]
        for u, v, cnt in edges:
            adjacency_list[u].append((v, cnt+1))
            adjacency_list[v].append((u, cnt+1))
    
        # Dijkstra
        distances = [INF for _ in range(n)]
        visited   = [False for _ in range(n)]
        
        distances[0] = 0
        
        # queue[*] = (distance, node_id)
        queue = [(0, 0)]
        
        while len(queue) > 0:
            d, s = heappop(queue)

            if visited[s]: continue
            visited[s] = True

            for t, w in adjacency_list[s]:
                distances[t] = min(distances[t], distances[s] + w)
                heappush(queue, (distances[t], t))
                        
        answer = 0
        
        # WARN: This does not count those original nodes 
        for u, v, cnt in edges:
            if distances[u] > maxMoves and distances[v] > maxMoves:
                continue
            elif distances[u] > maxMoves and distances[v] <= maxMoves:
                answer += maxMoves - distances[v]
            elif distances[u] <= maxMoves and distances[v] > maxMoves:
                answer += maxMoves - distances[u]
            elif distances[u] <= maxMoves and distances[v] <= maxMoves:
                answer += min(2*maxMoves - distances[u] - distances[v], cnt)
                
        # This adds only the original nodes
        for i in range(n):
            if distances[i] <= maxMoves:
                answer += 1
        
        return answer
        