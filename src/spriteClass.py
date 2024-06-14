import pygame
from src import helpers

# DEFINE COLOR AS 'b' or 'w'


class Piece(pygame.sprite.Sprite):
    def __init__(self, x, y, piecetype, color):
        super().__init__()
        self.image = pygame.image.load(helpers.getPiecePath(piecetype, color))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.type = piecetype
        self.color = color

