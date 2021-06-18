# https://leetcode.com/problems/valid-permutations-for-di-sequence/

class Solution:
    # len(s) <= 200
    def numPermsDISequence(self, s: str) -> int:
        n = len(s)

        # dp[i][j]: the i-th number is the j-th largest amongst a[0], a[1], ..., a[i]
        dp = [[0 for _ in range(n+1)] for _ in range(n+1)]

        # Base Case
        dp[0][0] = 1
        
        # Transition
        for i, sc in enumerate(s):
            # i --> i+1
            if sc == 'D':
                # Decreasing
                for j in range(i+1): # 0..i
                    dp[i+1][j+1] = dp[i+1][j] + dp[i][j]
            else:
                # Increasing
                for j in range(i+1, 0, -1): # i+1..1
                    dp[i+1][j-1] = dp[i+1][j] + dp[i][j-1]
        
            print(i, sc, dp[i+1])
            
        # answer = dp[n][0] + dp[n][1] + ... + dp[n][n]
        return sum(dp[n]) % (10**9 + 7)
        
'''
1
 \
  1
   \
    1
     \
      1   5
       \ / \
        1   20

dp[0]
| dp[1]
| | dp[2]
v v v
1 0 0 0 0 1 
  1 0 0 0 1 1
    1 0 0 1 2
      1 0 1 3
        1 1 4
          0 5
            5
'''