from tictactoe.lib.render import template
from tictactoe.ttt.models import Board

from django.shortcuts import get_object_or_404
import random

@template('ttt/index.html')
def index(request):
    return {}

@template('ttt/board.html')
def startGame(request):

    print "startGame"
    board = Board()
    if int (random.random() *2) == 1:
        board.computerPick()
    board.save()
    return dict(board=board, winner=None, noMoves=False)

@template('ttt/board.html')
def saveUserX(request, boardId, row, col):
    board = get_object_or_404(Board, pk=boardId)
    winner = None
    
    if board.setUserX(int(row), int(col)):
        winner='user'
    noMoves = board.noMoves()
    
    if not winner and not noMoves:
        if board.computerPick():
            winner='computer'
        
    board.save()
    noMoves = board.noMoves()
    
    return dict(board=board, winner=winner, noMoves=noMoves)
