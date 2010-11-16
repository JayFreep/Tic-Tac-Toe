from tictactoe.lib.render import template
from tictactoe.ttt.models import Board

from django.shortcuts import get_object_or_404

from computer import computerPick
import random

@template('ttt/index.html')
def index(request):
    return {}

@template('ttt/board.html')
def startGame(request):

    print "startGame"
    board = Board()
    if int (random.random() *2) == 1:
        computerPick(board)
    board.save()
    return dict(board=board)

@template('ttt/board.html')
def saveUserX(request, boardId, row, col):
    board = get_object_or_404(Board, pk=boardId)

    board.setUserX(int(row), int(col))
    computerPick(board)
    board.save()
    
    return dict(board=board)
