# https://leetcode.com/problems/closest-subsequence-sum/

def get_subarray_sums(nums, base=0):
    if len(nums) == 0:
        yield base
        return

    for k in get_subarray_sums(nums[1:], base):
        yield k
        yield k + nums[0]

    
class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        n = len(nums)

        lhs = sorted(get_subarray_sums([+k for k in nums[:n//2]]))
        rhs = sorted(get_subarray_sums([-k for k in nums[n//2:]], goal))
                
        ans = 10**100
        
        i = 0
        for j in range(len(rhs)):
            # Find the largest i such that lhs[i] <= rhs[j]
            while i+1 < len(lhs) and lhs[i+1] <= rhs[j]:
                i += 1
            
            if True:             ans = min(ans, abs(rhs[j] - lhs[i  ]))
            if i + 1 < len(lhs): ans = min(ans, abs(rhs[j] - lhs[i+1]))
            

        return ans
    
'''
2^40

x1 x2 x3 x4  1
 5 -7  3  5 -6 ~ 0

Exhaust: 5 x1 - 7 x2

(0, -7, 5, -2)
           **

Exhaust: -3 x3 - 5 x4 + 6

(6, 3, 1, -2)
          **

'''