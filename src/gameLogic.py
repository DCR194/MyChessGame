import os
from src import spriteClass
from src import helpers

allpieces = helpers.basicInitialize()

myKnight = spriteClass.Piece(50, 50, 'n', 'w')

def drawPieces(screen):
    for piece in allpieces:
        screen.blit(piece.image, piece.rect)

def resizePieces(newSize):
    for piece in allpieces:
        piece.resize(newSize)