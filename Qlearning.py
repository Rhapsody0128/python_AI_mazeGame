class Qnode():
	def __init__(self,x,y):
		self.Qvalue = [0,0,0,0]
		self.position = [x,y]

	def getBestWay(self):
		best = self.Qvalue[0]
		bestWay = 0
		print(self.Qvalue)
		for i in range(4):
			if self.Qvalue[i] >= best:
				best = self.Qvalue[i]
				bestWay = i
		return bestWay

	def allExplored(self):
		hasExplored = True
		for num in self.Qvalue:
			if num == 0:
				hasExplored = False
		return hasExplored
				
	def getNotExplore(self):
		notExplore = []
		for i in range(4):
			if self.Qvalue[i] == 0:
				notExplore.append(i)
		return notExplore
class Qtable ():
	def __init__(self,size):
		self.table = []
		self.route = []
		self.attenuationRate = 0.9
		self.createQtable(size)

	def record(self,qnode,direction):
		self.route.insert(0,[qnode,direction])

	def settle(self,reward):
		reward = reward
		print('結算')
		for qtable in self.route:
			print(qtable[0].Qvalue[qtable[1]])
			qtable[0].Qvalue[qtable[1]] = reward
			reward *= self.attenuationRate
		self.route = []
		
	def getQnode(self,position):
		return self.table[position[0]][position[1]]

	def createQtable(self,size):
		for i in range(size):
			row = []
			for j in range(size):
				qnode = Qnode(i,j)
				if i == 0 :
					qnode.Qvalue[0] = -1
				if j == 0 :
					qnode.Qvalue[3] = -1
				if i == size-1:
					qnode.Qvalue[2] = -1
				if j == size-1:
					qnode.Qvalue[1] = -1
				row.append(qnode)
			self.table.append(row)