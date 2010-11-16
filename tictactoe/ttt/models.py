from django.db import models

from django.contrib.auth.models import User
from computer import Computer

class Board(models.Model):
    matrix = models.CharField(max_length=9, default="         ")

    def asArray(self):
        return [self.matrix[0:3], self.matrix[3:6], self.matrix[6:9]]

    def pos (self, row, col):
        return row * 3 + col

    def setPos(self, row, col, symbol):
        pos = self.pos (row, col)
        self.setPosIndex(pos, symbol)

    def setPosIndex(self, index, symbol):
        tmp = list (self.matrix)
        tmp[index] = symbol
        self.matrix = ''.join(tmp)
        
    def canPlace(self, row, col):
        return self.canPlaceIndex(self.pos(row, col))
    
    def canPlaceIndex (self, index):
        return self.matrix[index] == ' '        
    
    def setUserX(self, row, col):
        self.setPos(row,col, 'X')
        return self.checkForWinner('X')

    def setComputerO(self, row, col):
        self.setPos(row,col, 'O')
        return self.checkForWinner('O')


    def computerPick(self):
        Computer().computerPick(self)
        return self.checkForWinner('O')

    def noMoves(self):
        return self.matrix.find(' ') == -1

    def checkForWinner(self, symbol):
        match = '%s%s%s' % (symbol,symbol, symbol)
        # check rows
        for each in self.asArray():
            if each == match:
                return True

        # check columns
        for colIndex in range (0,3):
            col = ''.join ([self.matrix[self.pos(0, colIndex)],
                              self.matrix[self.pos(1, colIndex)],
                              self.matrix[self.pos(2, colIndex)]])
            if col == match:
                return True

        #check diagnals
        center = self.matrix[4]
        if not center == symbol:
            return False
        if self.matrix[0] == center and self.matrix[8] == center:
            return True

        if self.matrix[2] == center and self.matrix[6] == center:
            return True
        

        return False


#class Game(models.Model):
    
#    user = models.ForeignKey(User, related_name = 'currentUser')
#    board = models.ForeignKey(Board)

