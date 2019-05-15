import random

#let 0-8 be the number of mines in a tile while 9 designates a mine

#x and y are the X and Y of the first tile clicked
#n and m are the dimensions of the matrix
#mines is the number of mines
#def generateBoard(x, y, n, m, mines):
def generate_matrix(n, m):
    ret = []
    for i in range(0, n):
        ret.append([])
        for j in range(0, m):
            ret[i].append(0)
    return ret


def print_matrix(mat):
    for i in range(0, len(mat)):
        for j in range(0, len(mat[i])):
            print(str(mat[i][j]) + " ", end='')
        print("\n", end='')
    print("\n", end='')


#fills a board with mines
def populate_board(x, y, n, m, mines, board):
    random.seed()
    if mines > n*m+1:
        print("Cannot have more mines than there are squares.")
        return
    for i in range(0, mines):
        #pick a random point
        rx = random.randint(0, n-1)
        ry = random.randint(0, m-1)
        while board[rx][ry] == 9 or (rx == x and ry == y): #shuffle again if that spot is already mined
            rx = random.randint(0, n-1)
            ry = random.randint(0, m-1)
        board[rx][ry] = 9


#print_matrix(generate_matrix(10, 10))


class MineSweeper:
    def __init__(self, rows, cols, num_mines):
        self.n = rows
        self.m = cols
        self.mines = num_mines
        self.board = generate_matrix(self.n, self.m)

    def populate_board(self, x, y):
        populate_board(x, y, self.n, self.m, self.mines, self.board)

x = MineSweeper(10, 10, 99)
print_matrix(x.board)
x.populate_board(5, 5)
print_matrix(x.board)

