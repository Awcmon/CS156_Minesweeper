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


def search(start, msgame):
    curNode = start
    status = minesweeper.status(msgame.n, msgame.m, msgame.mines, curNode.data)
    while status != 1:
        if status == -1:  # if we are at a losing state, go back
            curNode = curNode.parent
        else:  # if we are not at a losing state, but are not at a winning one, go down another branch
            for key in curNode.children.keys():
                if curNode.children[key].data == None:  #if we have not expanded this node
                    curNode.children[key].data = deepcopy(curNode.data) #fill it with data
                    curNode = curNode.children[key] #set it as the current node
                    if minesweeper.reveal_tile(key[0], key[1], msgame.n, msgame.m, msgame.board, curNode.data) == 9:
                        curNode = curNode.parent #if this leads to a losing gamestate, backtrack to the parent
                    else:
                        curNode.populate() #otherwise, populate this and continue
                    # minesweeper.print_matrix(curNode.data)
                    break #stop looping through the children
        status = minesweeper.status(msgame.n, msgame.m, msgame.mines, curNode.data) #recalculate the status
    return curNode #this should be the final solution, so return



game = minesweeper.MineSweeper(10, 10, 10)
game.select_tile(0,0)
print("The board: ")
minesweeper.print_matrix(game.board) #print the board
print("Initial revealed board: ")
minesweeper.print_matrix(game.gamestate) #print what the agent sees

root = Node(None, None) #create the root node
root.data = deepcopy(game.gamestate)
root.populate()
#print(root.children.keys())

print("Solution: ")
minesweeper.print_matrix(search(root, game).data) #search and print the results of the search

