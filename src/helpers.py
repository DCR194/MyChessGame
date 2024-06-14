import os
from src import spriteClass
from src import globals

def getPiecePath(type='p', color='w'):
    theme = ''
    if color == 'w':
        theme = 'lt'
    else:
        theme = 'dt'


    file = 'Chess_{}{}60.png'.format(type, theme)

    return os.path.join('src', 'assets', file)

def basicInitialize():
    allPieces = []
    for i in range(0, 2):
        for j in range(0, 8):
            if i == 0:
                allPieces.append(spriteClass.Piece(globals.boardX + j * globals.squareSize, 50 + i * globals.squareSize, 'p', 'b'))
            else:
                allPieces.append(spriteClass.Piece(globals.boardX + j * globals.squareSize, 50 + i * globals.squareSize, 'p', 'w'))

    return allPieces

