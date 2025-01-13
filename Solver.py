import numpy as np

class Solver:
    def __init__(self, board, curr=[0,0], guessed=[]):
        self.board = board
        self.curr = curr
        self.guessed = guessed
        self.solved = False

    def print(self):
        print(self.board)

    def check_solved(self):
        if 0 in self.board:
            return False
        return True

    def update_prev(self, a):
        self.board = prev_board
        self.curr = prev_curr
        self.guessed = prev_guessed
        self.guessed.append(a)

    def inc_curr(self):
        if self.curr[0] == self.curr[1] == 8:
            self.curr = [0,0]
            return False
        if self.curr[0] == 8:
            self.curr[0] = 0
            self.curr[1] += 1
            return True
        self.curr[0] += 1
        return True
            

    def get_row(self):
        return self.board[self.curr[0],:]

    def get_col(self):
        return self.board[:,self.curr[1]]

    def get_box(self):
        box = None
        if self.curr[0] in [0,1,2]:
            if self.curr[1] in [0,1,2]:
                box = 1
            if self.curr[1] in [3,4,5]:
                box = 2
            if self.curr[1] in [6,7,8]:
                box = 3
        if self.curr[0] in [3,4,5]:
            if self.curr[1] in [0,1,2]:
                box = 4
            if self.curr[1] in [3,4,5]:
                box = 5
            if self.curr[1] in [6,7,8]:
                box = 6
        if self.curr[0] in [6,7,8]:
            if self.curr[1] in [0,1,2]:
                box = 7
            if self.curr[1] in [3,4,5]:
                box = 8
            if self.curr[1] in [6,7,8]:
                box = 9

        if box == None:
            return None

        if box == 1:
            return self.board[0:3,0:3].flatten()
        if box == 2:
            return self.board[0:3,3:6].flatten()
        if box == 3:
            return self.board[0:3,6:].flatten()
        if box == 4:
            return self.board[3:6,0:3].flatten()
        if box == 5:
            return self.board[3:6,3:6].flatten()
        if box == 6:
            return self.board[3:6,6:].flatten()
        if box == 7:
            return self.board[6:,0:3].flatten()
        if box == 8:
            return self.board[6:,3:6].flatten()
        if box == 9:
            return self.board[6:,6:].flatten()

    def solve_step(self):
        guess_req = False
        while True:
            copy_old = np.copy(self.board)
            if self.board[self.curr[0],self.curr[1]] == 0:
                row = self.get_row()
                col = self.get_col()
                box = self.get_box()
                valid = []
                for i in range(1,10):
                    found = False
                    if i in row:
                        found = True
                    if i in col:
                        found = True
                    if i in box:
                        found = True
                    if found == False:
                        valid.append(i)
                if len(valid) == 1:
                    self.board[self.curr[0],self.curr[1]] = valid[0]
            if self.inc_curr() == False:
                if self.board.all() == copy_old.all():
                    guess_req = True
                break
        print(self.board)
        return guess_req
    
    def guess(self):
        pass


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
s1.print()
while not s1.check_solved():
    need_guess = s1.solve_step()
    if need_guess:
        s1.guess()

