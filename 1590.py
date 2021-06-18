# https://leetcode.com/problems/make-sum-divisible-by-p/

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n = len(nums)
        
        left_partial_sums  = [0 for _ in range(n+1)]
        right_partial_sums = [0 for _ in range(n+1)]
        
        for i in range(n):
            left_partial_sums[i+1] = (left_partial_sums[i] + nums[i]) % p

        for i in range(n, 0, -1):
            right_partial_sums[i-1] = (right_partial_sums[i] - nums[i-1]) % p

        lhs = {}
        rhs = {}
        
        for i in range(n+1):
            lhs[left_partial_sums[i]] = lhs.get(left_partial_sums[i], [])
            lhs[left_partial_sums[i]].append(i)
            rhs[right_partial_sums[i]] = rhs.get(right_partial_sums[i], [])
            rhs[right_partial_sums[i]].append(i)
                
        answer = n

        for m, left_ids in lhs.items():
            right_ids = rhs.get(m)
            if right_ids is None: continue
            
            j = 0
            for i in range(len(left_ids)):
                while j < len(right_ids) - 1 and right_ids[j] < left_ids[i]:
                    j += 1
                if right_ids[j] < left_ids[i]: break
                
                answer = min(answer, right_ids[j] - left_ids[i])
            
        if answer == n: return -1
        return answer

        
'''
Find the SMALLEST subarray a[k], a[k+1], ..., a[m] such that
a[k] + a[k+1] + ... + a[m] mod p = r, where r = sum(nums) % p


3  1  4  2
      X





-------->
0 3 4 8 10

<-------------
-10 -7 -6 -2 0


0 3 [4] 2 4
2 5  0 [4] 0
'''