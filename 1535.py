# https://leetcode.com/problems/find-the-winner-of-an-array-game/

class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        winners = [[arr[0], 0]]
        
        for a in arr[1:]:   
            last_winner = winners[-1]

            if a < last_winner[0]:
                last_winner[1] += 1
            else:
                winners.append([a, 1])
        
        for a, count in winners:
            if count >= k:
                return a
        
        return winners[-1][0]
        
    
    
'''
If k >= len(arr) - 1, then answer = max(arr)

If k == 1:
    1. The first element such that arr[i] > arr[i+1]
    2. The last element wins

If k == 2:
    1. The first element such that arr[i] > arr[i+1] AND arr[i] > arr[i+2]
    2. 

[1, 2, 3] --> 2





#X     X  X     X  X----------------------------------------
[2, 1, 3, 5, 4, 6, 7]

2 135467
2 354671
3 546712
5 467123
5 671234
6 712345
7 123456

[6, 5, 4, 7, 3, 2, 1]

6 547321
6 473215
6 732154
7 321546
7 215463
...

'''