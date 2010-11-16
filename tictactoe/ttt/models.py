from django.db import models

from django.contrib.auth.models import User


class Board(models.Model):
    matrix = models.CharField(max_length=9, default="         ")

    def asMatrix(self):
        return [self.matrix[0:3], self.matrix[3:6], self.matrix[6:9]]

    def setUserX(self, row, col):
        tmp = list (self.matrix)
        tmp[row * 3 + col] = 'X'
        self.matrix = ''.join(tmp)


#class Game(models.Model):
    
#    user = models.ForeignKey(User, related_name = 'currentUser')
#    board = models.ForeignKey(Board)

