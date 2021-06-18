# Find an array u[0], u[1], ..., u[n-1] satisfying
# u[i] is the smallest r such that
#   "nums[i], nums[i+1], ..., nums[r]" have k distinct members
# or if r == n, such r does not exist.
def subsolve(nums: List[int], k: int, n: int) -> List[int]:
    u = [n for _ in range(n)]

    # Begin the game
    distinct_count = 0
    occurrences = [0 for _ in range(n+1)]
    for j in range(n):
        occurrences[nums[j]] += 1
        if occurrences[nums[j]] == 1:
            distinct_count += 1

        if distinct_count == k:
            u[0] = j
            break

    for i in range(1, n):
        occurrences[nums[i-1]] -= 1
        if occurrences[nums[i-1]] == 0:
            distinct_count -= 1

        j = u[i-1]
        while j < n and distinct_count < k:
            j += 1
            if j == n: break
            occurrences[nums[j]] += 1
            if occurrences[nums[j]] == 1:
                distinct_count += 1

        u[i] = j

    return u

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        u1 = subsolve(nums, k,   n)
        u2 = subsolve(nums, k+1, n)
        
        return sum([x-y for x, y in zip(u2, u1)])