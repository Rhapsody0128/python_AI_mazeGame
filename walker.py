from math import e
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
		self.face = random.randint(0,4)%4
		self.step = 0
		self.position = self.maze.start.position
		self.blocked = 0
		self.clockwise = False
		self.node = RouteNode(None,self.position)
		
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
		if self.blocked == 0 :
			if random.random()>0.5:
				self.clockwise = True
		if self.clockwise == True :
			self.face += 1
			self.face = self.face % 4
			self.blocked += 1
			print('順時轉')
		else:
			self.face -= 1
			self.face = abs(self.face % 4)
			self.blocked += 1
			print('逆時轉')

class Drawer(Walker):
	def __init__(self,name,maze):
		super().__init__(name,maze)
		print('起始點'+str(self.position))
	def judgeCanWalk(self):		
		if self.maze.getGrid(self.position).wall[self.face]!= 2 and self.maze.getGrid(self.getNextPosition()).visit < 1 :
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
		if self.judgeCanWalk():
			nextPosition = self.getNextPosition()
			print(f"從{self.position}走到{nextPosition}")

			newNode = RouteNode(self.node,nextPosition)
			self.node = newNode

			self.action()
			self.position = self.getNextPosition()
			self.step += 1
			self.maze.getGrid(self.position).visit += 1
			self.blocked = 0
			
			if random.random()>=4:
				self.turn()
				print(f"任性轉彎到{self.face}")
		else:
			self.turn()

	def autoWalk(self):
		self.walk()
		if self.judgeArrivedGoal() :
			self.backNode()
			self.autoWalk()
		elif self.blocked > 4 :
			if self.node.lastNode == None :
				self.end()
			else:
				self.backNode()
				self.autoWalk()
		else: 
			self.autoWalk()

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

	def backNode(self):
		print('回上一格')
		self.node = self.node.lastNode
		self.position = self.node.position

	def end(self):
		print('結束')



class RouteNode():
	def __init__(self,lastNode,position):
		self.lastNode = lastNode
		self.position = position