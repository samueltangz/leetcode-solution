# https://leetcode.com/problems/wiggle-sort-ii/

class Solution:
    def __init__(self):
        self.m = [0 for _ in range(5001)]
        self.j = 0
        
    def next(self):
        while self.m[self.j] == 0:
            self.j += 1
        self.m[self.j] -= 1
        return self.j
        
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        
        # Fall into buckets
        for k in nums: self.m[k] += 1

        # (n = 5) 3 5 2 4 1
        # (n = 6) 3 6 2 5 1 4
        
        for k in range((n-1) & 0xfffe, -1, -2):
            j = self.next()
            nums[k] = j
            
        for k in range((n-1) | 1,      -1, -2):
            if k >= n: continue
                
            j = self.next()
            nums[k] = j
            