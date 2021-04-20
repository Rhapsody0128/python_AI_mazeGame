
wall:{
	0:'empty',
	1:'wall',
	2:'outerWall',
	3:'door'
}

class Grid():
	def __init__(self,size,x,y,index):
		self.wall = [1,1,1,1]
		self.index = index
		self.position = [x,y]
		self.visit = 0