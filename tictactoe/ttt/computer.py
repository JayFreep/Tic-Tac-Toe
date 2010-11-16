# The computer gets to pick there spot

# Assume for now that computer is 'O' and user is 'X' so we don't have to pass some variables around
import random

class Computer(object):

    def computerPick(self,board):
    
        # take the center if it's open
        if board.canPlace(1,1):
            board.setPos(1,1, 'O')
            return

        # see if we can find a win first
        if self.findWin(board):
            return

        #see if we can find a block
        # if we can't win and can't block just pick a random placement
        if not self.findBlock(board):
            #print "no Block"
            pos = int (8 * random.random())
            #print pos
            while not board.canPlaceIndex(pos):
                pos = int (8 * random.random())
                #print pos

            board.setPosIndex(pos, 'O')

    # Look for two in a row fomr our potential three in a rows and
    # either win or block there
    def findSpot(self, board, match):
        for index in range (len(solutions)):
            check = solutions[index]
            for possible in check:
                vote = 0
                for position in possible:
                    if board.matrix[position] == match:
                        vote = vote + 1
                if vote == 2:
                    if board.canPlaceIndex(index):
                        print "block at %d" % index
                        board.setPosIndex(index, 'O')
                        return True
        return False

    def findWin(self, board):
        return self.findSpot (board, 'O')

    def findBlock(self, board):
        return self.findSpot(board,'X')

# for each index, what are the corresponding positions that could yield three in a row
solutions = [
    [ [1,2], [3,6], [4,8] ],
    [ [0,2], [4,7] ],
    [ [0,1], [4,6], [5,8] ],
    [ [0,6], [4,5] ],
    [ [0,8], [1,7], [2,6], [3,5] ],
    [ [2,8], [3,4] ],
    [ [0,3], [2,4], [7,8] ],
    [ [1,4], [6,8] ],
    [ [0,4], [2,5], [6,7] ]
    ]
     
