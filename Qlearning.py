
import math
class Qnode():
	def __init__(self,x,y):
		self.Qvalue = [0,0,0,0]
		self.position = [x,y]

	def getBestWay(self):
		best = self.Qvalue[0]
		bestWay = 0
		for i in range(4):
			if self.Qvalue[i] >= best:
				best = self.Qvalue[i]
				bestWay = i
		return bestWay
class Qtable ():
	def __init__(self,size):
		self.table = []
		self.route = []
		self.attenuationRate = 0.95
		self.createQtable(size)

	def record(self,qnode,direction):
		self.route.insert(0,[qnode,direction])

	def settle(self,reward):
		reward = reward
		for qtable in self.route:
			reward *= self.attenuationRate
			qtable[0].Qvalue[qtable[1]] += reward
		self.route = []
		

	def getQnode(self,position):
		return self.table[position[0]][position[1]]

	def createQtable(self,size):
		for i in range(size):
			row = []
			for j in range(size):
				qnode = Qnode(i,j)
				row.append(qnode)
			self.table.append(row)
	