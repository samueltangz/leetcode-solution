class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)

        # make an adjacency list such that s->t represent that
        # s can be jumped to t
        
        adjacency_list = [[] for _ in range(n)]
        
        for s in range(n):
            # Jump left
            for i in range(1, d+1):
                t = s - i
                if t < 0: break
                if arr[s] <= arr[t]: break
                
                adjacency_list[s].append(t)
            
            # Jump right
            for i in range(1, d+1):
                t = s + i
                if t >= n: break
                if arr[s] <= arr[t]: break
                
                adjacency_list[s].append(t)

        # find the maximum number of jumps
        
        tagged_heights = sorted(enumerate(arr), key=lambda u: u[1], reverse=True)
        max_jumps = [1 for _ in range(n)]
                
        for s, height in tagged_heights:
            for t in adjacency_list[s]:
                # s --> t
                max_jumps[t] = max(max_jumps[t], max_jumps[s] + 1)
        
        print(max_jumps)
        
        return max(max_jumps)