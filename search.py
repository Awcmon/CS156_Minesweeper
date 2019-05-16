import minesweeper
from copy import copy, deepcopy

#Depth first search with backtracking
class Node:
    def __init__(self, parent, key):
        self.parent = parent
        if not (self.parent is None):
            parent.children[key] = self
        self.data = None
        self.children = {}

    #populate self with children
    def populate(self):
        for i in range(0, len(self.data)):
            for j in range(0, len(self.data[i])):
                if self.data[i][j] == '?':
                    node = Node(self, (i, j))

#generate the children of this parent
def populate_parent(parent):
    for i in range(0, len(parent.data)):
        for j in range(0, len(parent.data[i])):
            if parent.data[i][j] == '?':
                node = Node(parent, (i, j))

#search for a win state from this node
"""
def search(node, board):
    populate_parent(node, node.data)
    for key in node.children.keys():
        if node.children[key].data == None:
            node.children[key].data = deepcopy(node.data)
            if 
"""



game = minesweeper.MineSweeper(10, 10, 10)
#game.populate_board(4, 4)
game.select_tile(0,0)
minesweeper.print_matrix(game.board)
minesweeper.print_matrix(game.gamestate)

root = Node(None, None)
root.data = deepcopy(game.gamestate)
root.populate()
print(root.children.keys())