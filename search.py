import minesweeper
from copy import copy, deepcopy

#Depth first search with backtracking
class Node:
    def __init__(self, parent, data):
        self.parent = parent
        if not (self.parent is None):
            parent.children.append(self)
        self.data = data
        self.children = []



game = minesweeper.MineSweeper(10, 10, 10)
#game.populate_board(4, 4)
game.select_tile(0,0)
minesweeper.print_matrix(game.board)
minesweeper.print_matrix(game.gamestate)