# https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/

# Non-optimal implementation for disjoint set
class DisjointSet:
    def __init__(self, n):
        self.n = n
        self.ids = [i for i in range(n)]
        self.sets = [[i] for i in range(n)]
        
    def join(self, u, v):
        if self.connected(u, v): return
        
        iu = self.ids[u]
        iv = self.ids[v]
        siu = self.sets[iu]
        siv = self.sets[iv]
        
        if len(siu) < len(siv):
            u, v = v, u
            iu, iv = iv, iu
            siu, siv = siv, siu
            
        for k in siv:
            self.ids[k] = iu
        
        self.sets[iu] += self.sets[iv]
        self.sets[iv] = []
            
    def connected(self, u, v):
        return self.ids[u] == self.ids[v]

class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        '''
        Approach: Disjoint set
        1. Sort the queries with ascending limits
        2. Start with n independent sets
        3. for each increasing limit, join the (unjoined) edges with distance < limit
        4. answer if the disjoint set is the same set
        '''
        s = DisjointSet(n)
        
        edges = sorted(edgeList, key=lambda e: e[2])
        
        tagged_queries = [q[:] + [i] for i, q in enumerate(queries)]
        tagged_queries = sorted(tagged_queries, key=lambda q: q[2])
        
        answer = [None for _ in queries]
        
        ei = 0
        for u, v, l, ind in tagged_queries:
            while ei < len(edges) and edges[ei][2] < l:
                s.join(edges[ei][0], edges[ei][1])
                ei += 1
            answer[ind] = s.connected(u, v)
        
        return answer
        