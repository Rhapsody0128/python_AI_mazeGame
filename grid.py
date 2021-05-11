import pygame as pg
import random

wall={
	0:'empty',
	1:'wall',
	2:'outerWall',
	3:'door'
}

class Grid(pg.sprite.Sprite):
	def __init__(self,size,x,y,index,map):
		pg.sprite.Sprite.__init__(self)

		self.map = map
		self.wall = [1,1,1,1]
		self.index = index
		self.position = [x,y]
		self.visit = 0
		self.gridSize = 50
		self.wallSize = 1
		self.color = 'gray'
		self.drawGrid()
		self.drawWall()

	def drawGrid(self):
		self.image = pg.Surface([self.gridSize, self.gridSize])
		self.image.fill(self.color)
		self.rect = self.image.get_rect()
		self.rect.x = (self.position[0]) * (self.gridSize)
		self.rect.y = (self.position[1]) * (self.gridSize)
		pg.display.update()

	def drawWall(self):
		for i in range(4) :
			wall = self.wall[i]
			pg.draw.line(self.image,self.getWallColor(wall), self.getWallDrawPosition(i)[0], self.getWallDrawPosition(i)[1], self.wallSize)


		pg.display.update()
	
	def getWallDrawPosition(self,face):
		if face == 0 :
			return [(0,0),(self.gridSize-self.wallSize/2,0)]
		if face == 1 :
			return [(self.gridSize-self.wallSize/2,0),(self.gridSize-self.wallSize/2,self.gridSize-self.wallSize/2)]
		if face == 2 :
			return [(self.gridSize-self.wallSize/2,self.gridSize-self.wallSize/2),(0,self.gridSize-self.wallSize/2)]
		if face == 3 :
			return [(0,self.gridSize-self.wallSize/2),(0,0)]

	def getWallColor(self,wall):
			if wall == 0:
				return self.color
			if wall == 1:
				return 'red'
			if wall == 2:
				return 'blue'
			if wall == 3:
				return 'green'
