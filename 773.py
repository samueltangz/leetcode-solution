# https://leetcode.com/problems/sliding-puzzle/

def encodeBoard(board: List[List[int]]) -> int:
    out = 0
    for i in range(2):
        for j in range(3):
            out += board[i][j] * 6**(3 * i + j)
    return out

def copy(board: List[List[int]]) -> List[List[int]]:
    return [[board[i][j] for j in range(3)] for i in range(2)]

def move(board: List[List[int]]) -> List[List[List[int]]]:
    moves = []
    
    ds = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    for x in range(2):
        for y in range(3):
            if board[x][y] != 0: continue
            for dx, dy in ds:
                if x + dx < 0: continue
                if x + dx >= 2: continue
                if y + dy < 0: continue
                if y + dy >= 3: continue
                
                tmp_move = copy(board)
                tmp_move[x][y] = tmp_move[x+dx][y+dy]
                tmp_move[x+dx][y+dy] = 0
                moves.append(tmp_move)
    return moves
                
                
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        distances = [-1 for _ in range(6**6)]
    
        s = [[1, 2, 3], [4, 5, 0]]
        t = copy(board)
        
        es = encodeBoard(s)
        et = encodeBoard(t)

        queue = [s]
        distances[es] = 0
        
        while len(queue) > 0:
            u = queue.pop(0)
            eu = encodeBoard(u)
            for v in move(u):
                ev = encodeBoard(v)
                if distances[ev] != -1: continue
                distances[ev] = distances[eu] + 1
                queue.append(v)
                
        return distances[et]