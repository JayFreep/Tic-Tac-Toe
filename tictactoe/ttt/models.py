from django.db import models

from django.contrib.auth.models import User
from computer import computerPick

class Board(models.Model):
    matrix = models.CharField(max_length=9, default="         ")

    def asArray(self):
        return [self.matrix[0:3], self.matrix[3:6], self.matrix[6:9]]

    def pos (self, row, col):
        return row * 3 + col
    
    def setUserX(self, row, col):
        pos = self.pos (row, col)
        tmp = list (self.matrix)
        tmp[pos] = 'X'
        self.matrix = ''.join(tmp)
        return self.checkForWinner('X')

    def computerPick(self):
        computerPick(self)
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

        #check diagnols
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

