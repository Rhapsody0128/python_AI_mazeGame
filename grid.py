import pygame

wall:{
	0:'empty',
	1:'wall',
	2:'outerWall',
	3:'door'
}

class Grid(pygame.sprite.Sprite):
	def __init__(self,size,x,y,index,surface):
		super().__init__()
		self.rect.topleft = (x, y)
		self.width = 1
		self.height  = 1
		self.wall = [1,1,1,1]
		self.index = index
		self.position = [x,y]
		self.visit = 0
		pygame.draw.rect(self.surface, 'black', [x, y, 1,1], 0.5)