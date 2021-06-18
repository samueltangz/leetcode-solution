import itertools

class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])

        # partial_sum[i][j]
        # = sum[0][0] + sum[0][1] + ... + sum[0][j-1]
        #   + sum[1][0] + sum[1][1] + ... + sum[1][j-1]
        #   + ...
        #   + sum[i-1][0] + sum[i-1][1] + ... + sum[i-1][j-1]
        partial_sum = [[0 for _ in range(n+1)] for _ in range(m+1)]

        for x, y in itertools.product(range(m), range(n)):
            partial_sum[x+1][y+1]  = mat[x][y]
            partial_sum[x+1][y+1] += partial_sum[x][y+1] + partial_sum[x+1][y]
            partial_sum[x+1][y+1] -= partial_sum[x][y]
        
        ans = 0
        
        # Top-left corner
        for x, y in itertools.product(range(m), range(n)):
            for k in range(ans, min(m-x, n-y) + 1):
                subsum  = partial_sum[x+k][y+k]
                subsum -= partial_sum[x  ][y+k]
                subsum -= partial_sum[x+k][y  ]
                subsum += partial_sum[x  ][y  ]
                if subsum <= threshold: # sum to be calculated
                    ans = k
                else:
                    break
        
        return ans