RIGHT = 0
DOWN  = 1
LEFT  = 2
UP    = 3

deltas = [
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0)
]

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        nums = [[None for _ in range(n)] for _ in range(n)]
        
        x, y, d = 0, 0, RIGHT
        for step in range(n**2):
            nums[x][y] = step+1
            
            # move
            dx, dy = deltas[d]
            x2, y2 = x+dx, y+dy
            
            if 0 <= x2 < n and 0 <= y2 < n and nums[x2][y2] is None:
                x, y = x2, y2
            else:
                # rotate and move    
                d = (d + 1) % 4
                dx, dy = deltas[d]
                x2, y2 = x+dx, y+dy
        
                x, y = x2, y2

        return nums