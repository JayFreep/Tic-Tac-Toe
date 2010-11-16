Simple Django based Tic-Tac-Toe game

The computer is 'O', the user is 'X'

The UI is nothing special.  Just click "X" where you want to put an X and the computer will respond.  But it works as a web app in Django

Random selection of who goes first

The AI for the computer if fairly brute force:
xs
    1. First we try to save in the center, if we can.  That will be either the opening move or the computer's first counter
    2. Next, the computer will try to find two "O" n a row so it can place the third and win
    3. If not, the computer will try to find two "X" in a row to block the user from winning
    4 If not any of the above, simply pick a random placement 

The UI will occasionally lose so it's not perfect but it works pretty well in most cases 
