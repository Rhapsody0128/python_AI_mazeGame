from maze import Maze
import random
import pygame as pg

face={
	0:'up',
	1:'right',
	2:"down",
	3:"left"
}
class Walker():
	def __init__(self,name,maze):
		self.maze = maze
		self.name = name
		self.face = random.randint(0,4)
		self.step = 0
		self.position = self.maze.start.position
		self.blocked = 0

	def walk(self):
		if self.judgeCanWalk():
			nextPosition = self.getNextPosition()
			print(f"從{self.position}走到{nextPosition}")
			self.action()
			self.position = self.getNextPosition()
			self.step += 1
			self.maze.getGrid(self.position).visit += 1
		else:
			self.turn()


	def action(self):
		print('走下一個')

	def judgeCanWalk(self):
		if self.maze.getGrid(self.position).wall[self.face] == 0:
			return True
		else :
			return False

	def getNextPosition(self):
		if self.face == 0:
			nextPosition = [self.position[0]-1,self.position[1]]
		elif self.face == 1:
			nextPosition = [self.position[0],self.position[1]+1]
		elif self.face == 2:
			nextPosition = [self.position[0]+1,self.position[1]]
		elif self.face == 3:
			nextPosition = [self.position[0],self.position[1]-1]	
		return nextPosition

	def turn(self):
		random1 = random.random()
		self.blocked += 1
		if random1 > 0.5 :
			self.face += 1
			self.face = self.face % 4
			print('向右轉')
		else:
			self.face -= 1
			self.face = abs(self.face % 4)
			print('向左轉')

class Drawer(Walker):
	def __init__(self,name,maze):
		super().__init__(name,maze)
		print('起始點'+str(self.position))

	def judgeCanWalk(self):
		if self.maze.getGrid(self.position).wall[self.face] == 1 and self.maze.getGrid(self.getNextPosition()).visit < 1:
			print('現在方向'+str(self.face))
			print('面對牆壁是'+str(self.maze.getGrid(self.position).wall[self.face]))
			print('可以走')
			return True
		else :
			print('現在方向'+str(self.face))
			print('面對牆壁是'+str(self.maze.getGrid(self.position).wall[self.face]))
			print('不能走')
			return False
		
	def walk(self):
		print(self.judgeCanWalk())
		if self.judgeCanWalk():
			nextPosition = self.getNextPosition()
			print(f"從{self.position}走到{nextPosition}")
			self.action()
			self.position = self.getNextPosition()
			self.step += 1
			self.maze.getGrid(self.position).visit += 1
			rand = random.random()
			if self.judgeArrivedGoal():
				self.end()
			if rand>=0.7:
				self.turn()
				print(f"任性轉彎到{self.face}")
		else:
			self.turn()

	def action(self):
		try:
			self.maze.getGrid(self.position).wall[self.face] = 0
			self.maze.getGrid(self.getNextPosition()).wall[(self.face+2)%4] = 0
			print('打破牆壁')
		except:
			print('撞牆')

	def judgeArrivedGoal(self):
		if self.position == self.maze.goal.position:
			print('到達終點')
			return True
		else:
			return False

	def end(self):
		self.drawer = Drawer("Drawer",self.maze)


