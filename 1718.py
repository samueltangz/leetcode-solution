# https://leetcode.com/problems/construct-the-lexicographically-largest-valid-sequence/

def plug(numbers, used, n, remaining):
    if remaining == 0: return numbers

    # Find the leftmost element that has nothing
    k = numbers.index(None)
    
    # used[i] = n-i is already used
    for i, u in enumerate(used):
        if u: continue

        # Try to plug m in
        m = n-i
        
        if m == 1:
            numbers[k] = m
            used[i] = True

            res = plug(numbers, used, n, remaining-1)
            if res is not None: return res

            numbers[k] = None
            used[i] = False
        else:
            if k + m < 2*n-1 and numbers[k + m] is None:
                numbers[k    ] = m
                numbers[k + m] = m
                used[i] = True

                res = plug(numbers, used, n, remaining-1)
                if res is not None: return res

                numbers[k    ] = None
                numbers[k + m] = None
                used[i] = False
            
class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        numbers = plug(
            [None for _ in range(2*n-1)],
            [False for _ in range(n)],
            n,
            n
        )
        return numbers