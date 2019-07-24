import pygame as py
from flat import *
from random import randint


class level:
	def __init__(self, window):
		self.platforms = []
		for i in range(1):
			x = randint(0, 1000)
			y = randint(0, 600)
			self.platforms.append(Flat())
			self.platforms[-1].xPos = x
			self.platforms[-1].yPos = y
			self.platforms[-1].moveRect()
					
	def drawLevel(self, window):
		for element in self.platforms:
			element.draw(window)
