import numpy as np

class Solver:
    def __init__(self, board):
        self.board = board

    def get_box(self, x, y):
        if x in [0,1,2]:
            if y in [0,1,2]:
                return self.board[0:3,0:3].flatten()
            if y in [3,4,5]:
                return self.board[0:3,3:6].flatten()
            if y in [6,7,8]:
                return self.board[0:3,6:].flatten()
        if x in [3,4,5]:
            if y in [0,1,2]:
                return self.board[3:6,0:3].flatten()
            if y in [3,4,5]:
                return self.board[3:6,3:6].flatten()
            if y in [6,7,8]:
                return self.board[3:6,6:].flatten()
        if x in [6,7,8]:
            if y in [0,1,2]:
                return self.board[6:,0:3].flatten()
            if y in [3,4,5]:
                return self.board[6:,3:6].flatten()
            if y in [6,7,8]:
                return self.board[6:,6:].flatten()


    def valid(self, x, y, n):
        row = self.board[x,:]
        col = self.board[:,y]
        box = self.get_box(x, y)
        if n in row:
            return False
        if n in col:
            return False
        if n in box:
            return False
        return True
    

    def solve(self):
        for x in range(9):
            for y in range(9):
                if self.board[x,y] == 0:
                    for n in range(1,10):
                        if self.valid(x,y,n):
                            board[x,y] = n
                            self.solve()
                            board[x,y] = 0
                    return
        print(board)

board = np.array([[0,4,0,0,0,7,0,0,0],
                  [0,0,1,8,9,4,0,0,0],
                  [8,2,7,0,6,3,0,9,0],
                  [0,0,0,7,0,8,0,0,4],
                  [0,8,5,0,4,9,6,0,7],
                  [0,7,0,6,5,1,2,8,0],
                  [0,9,6,3,8,2,5,0,0],
                  [7,0,0,9,1,0,0,0,0],
                  [0,0,0,0,0,5,0,0,3]])

s1 = Solver(board)
s1.solve()

