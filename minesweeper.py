import random

#let 0-8 be the number of mines in a tile while 9 designates a mine

#x and y are the X and Y of the first tile clicked
#n and m are the dimensions of the matrix
#mines is the number of mines
#def generateBoard(x, y, n, m, mines):
def generate_matrix(n, m, default_val):
    ret = []
    for i in range(0, n):
        ret.append([])
        for j in range(0, m):
            ret[i].append(default_val)
    return ret


def print_matrix(mat):
    for i in range(0, len(mat)):
        for j in range(0, len(mat[i])):
            print(str(mat[i][j]) + " ", end='')
        print("\n", end='')
    print("\n", end='')

def clamp(x, minv, maxv):
    return max(min(x, maxv), minv)

#returns the number of adjacent mines at a particular tile
def sum_adj_mines(x, y, n, m, board):
    if board[x][y] == 9:
        return 9
    ret = 0
    for i in range(clamp(x-1, 0, n-1), clamp(x+1, 0, n-1)+1):
        for j in range(clamp(y-1, 0, m-1), clamp(y+1, 0, m-1)+1):
            if board[i][j] == 9 and not (i == x and j == y): #if the square is a mine and is not the square in question
                ret += 1
    return ret

#fills a board with mines
def populate_board(x, y, n, m, mines, board):
    random.seed()
    if mines > n*m+1:
        print("Cannot have more mines than there are squares.")
        return
    #place all the mines
    for i in range(0, mines):
        #pick a random point
        rx = random.randint(0, n-1)
        ry = random.randint(0, m-1)
        while board[rx][ry] == 9 or (rx == x and ry == y): #shuffle again if that spot is already mined
            rx = random.randint(0, n-1)
            ry = random.randint(0, m-1)
        board[rx][ry] = 9
    #fill non-mine squares with number of adj mines
    for i in range(0, len(board)):
        for j in range(0, len(board[i])):
            board[i][j] = sum_adj_mines(i, j, n, m, board)


def reveal_tile(x, y, n, m, board, gamestate):
    if gamestate[x][y] == '?':
        gamestate[x][y] = board[x][y];
        if board[x][y] == 0:
            for i in range(clamp(x - 1, 0, n - 1), clamp(x + 1, 0, n - 1) + 1):
                for j in range(clamp(y - 1, 0, m - 1), clamp(y + 1, 0, m - 1) + 1):
                    if gamestate[i][j] == '?' and not (i == x and j == y):
                        reveal_tile(i, j, n, m, board, gamestate)
    return gamestate[x][y]

#return game status.
#-1 for loss
#0 for ongoing
#1 for win
def status(n, m, mines, gamestate):
    unknownsum = 0
    for i in range(0, n):
        for j in range(0, m):
            if gamestate[i][j] == 9:
                return -1
            elif gamestate[i][j] == '?':
                unknownsum += 1
    if(unknownsum == mines):
        return 1
    else:
        return 0

#print_matrix(generate_matrix(10, 10))


class MineSweeper:
    def __init__(self, rows, cols, num_mines):
        self.n = rows
        self.m = cols
        self.mines = num_mines
        self.board = generate_matrix(self.n, self.m, 0)
        self.gamestate = generate_matrix(self.n, self.m, '?')
        self.populated = False

    def populate_board(self, x, y):
        populate_board(x, y, self.n, self.m, self.mines, self.board)

    def select_tile(self, x, y):
        if not self.populated:
            self.populate_board(x, y)
            self.populated = True
            reveal_tile(x, y, self.n, self.m, self.board, self.gamestate)
        else: #reveal tiles
            reveal_tile(x, y, self.n, self.m, self.board, self.gamestate)

"""
game = MineSweeper(10, 10, 10)
#game.populate_board(4, 4)
game.select_tile(0,0)
print_matrix(game.board)
print_matrix(game.gamestate)
"""
