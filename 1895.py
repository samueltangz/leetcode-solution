def isMagicSquare(grid: List[List[int]], x: int, y: int, k: int) -> bool:    
    # If it is a magic square, all of the row/column/diagonal sums to s
    s = sum(grid[x][y:y+k])
    
    for i in range(k):
        # row sums are the same
        if sum([grid[x+i][y+j] for j in range(k)]) != s: return False
        # column sums are the same
        if sum([grid[x+j][y+i] for j in range(k)]) != s: return False
    
    # diagonal sums are the same
    if sum([grid[x+i][y+i]     for i in range(k)]) != s: return False
    if sum([grid[x+i][y+k-1-i] for i in range(k)]) != s: return False
    
    return True

class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        ans = 1

        m, n = len(grid), len(grid[0])
        
        # isMagicSquare will be called O(max(m, n)^3) times
        for x in range(m):
            for y in range(n):
                for k in range(ans+1, min(m-x, n-y)+1):
                #              ***** for optimization
                    assert k <= m-x
                    assert k <= n-y
                    if not isMagicSquare(grid, x, y, k): continue
                    ans = max(ans, k)
        
        return ans