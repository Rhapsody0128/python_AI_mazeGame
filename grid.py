import pygame as pg
import random

wall:{
	0:'empty',
	1:'wall',
	2:'outerWall',
	3:'door'
}

class Grid(pg.sprite.Sprite):
	def __init__(self,size,x,y,index):
		pg.sprite.Sprite.__init__(self)

		self.wall = [1,1,1,1]
		self.index = index
		self.position = [x,y]
		self.visit = 0
		self.girdSize = 50
		self.wallSize = 3
		self.color = 'gray'
		self.drawGrid()

	def drawGrid(self):
		self.image = pg.Surface([self.girdSize, self.girdSize])
		self.image.fill(self.color)
		self.rect = self.image.get_rect()
		self.rect.x = self.position[0] * (self.girdSize+self.wallSize)
		self.rect.y = self.position[1] * (self.girdSize+self.wallSize)
		pg.display.update()

	def drawWall(self):
		self.image.line