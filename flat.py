import pygame as py
from sprites import tiles


class Flat:
    def __init__(self):
        self.xPos = 0
        self.yPos = 0
        self.image = tiles[0]
        self.rect = self.image.get_rect()
        self.moveRect()

    def draw(self, display):
        display.blit(self.image, (self.xPos, self.yPos))

    def moveRect(self):
        self.rect.x = self.xPos
        self.rect.y = self.yPos
