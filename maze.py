
import random

from grid import Grid

class Maze():
	def __init__(self,size):
		self.size = size
		self.maze = []
		self.start = [random.randint(0,size-2)+1,0]
		self.goal = [random.randint(0,size-2)+1,self.size-1]
		self.createMaze(self.size)

	def getGrid(self,position):
		return self.maze[position[0]][position[1]]

	def createMaze(self,size):
		index = 0
		for i in range(size):
			row = []
			for j in range(size):
				grid = Grid(size,j,i,index)
				if i == 0 :
					grid.wall[0] = 2
				if j == 0 :
					grid.wall[3] = 2
				if i == size-1:
					grid.wall[2] = 2
				if j == size-1:
					grid.wall[1] = 2
				row.append(grid)
				index += 1
			self.maze.append(row)

	def drawMaze(self):
		TXT = open('maze.txt','w')
		for mazeRow in self.maze:
			for mazeCol in mazeRow:
				TXT.write(str(mazeCol.wall))
			TXT.write('\n')
		TXT.close()

z = Maze(4)
z.drawMaze()