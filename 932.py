# https://leetcode.com/problems/beautiful-array/

class Solution:
    def subbeautifulArray(self, arr: List[int]) -> List[int]:
        n = len(arr)
        if n <= 1: return arr[:]
        return self.subbeautifulArray(arr[0::2]) + self.subbeautifulArray(arr[1::2])
        
    def beautifulArray(self, n: int) -> List[int]:
        return self.subbeautifulArray(list(range(1, n+1)))