import pygame

class Piece(pygame.sprite.Sprite):
    def __init__(self, color, type, position, x, y):
        self.color = color
        self.type = type
        self.position = position
        self.x = x
        self.y = y
        

