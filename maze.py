
import random

from grid import Grid
import pygame as pg
import tkinter as tk


class Maze():
	def __init__(self,size,screen):
		self.screen = screen
		self.size = size
		self.maze = []
		self.start = [random.randint(0,size-1),0]
		self.goal = [random.randint(0,size-1),self.size-1]
		self.gridGroup = pg.sprite.Group()
		self.map = pg.Surface((self.screen.get_size()[0],self.screen.get_size()[1]))
		self.map.fill('white')
		self.createMaze(self.size)
		self.updateAllWall()

		# self.screen.blit(self.map,[int((tk.Tk().winfo_screenwidth()-tk.Tk().winfo_screenheight())/2),0])
		self.screen.blit(self.map,[0,0])
	def getGrid(self,position):
		return self.maze[position[0]][position[1]]

	def createMaze(self,size):
		index = 0
		for i in range(size):
			row = []
			for j in range(size):
				grid = Grid(size,j,i,index,self.map)
				if i == 0 :
					grid.wall[0] = 2
				if j == 0 :
					grid.wall[3] = 2
				if i == size-1:
					grid.wall[2] = 2
				if j == size-1:
					grid.wall[1] = 2
				row.append(grid)
				grid.drawWall()
				self.gridGroup.add(grid)
				self.gridGroup.draw(self.map)
				index += 1
			self.maze.append(row)

	def drawMaze(self):
		TXT = open('maze.txt','w')
		for mazeRow in self.maze:
			for mazeCol in mazeRow:
				TXT.write(str(mazeCol.wall))
			TXT.write('\n')
		TXT.close()

	def updateAllWall(self):
		for mazeRow in self.maze:
			for mazeCol in mazeRow:
				mazeCol.drawWall()