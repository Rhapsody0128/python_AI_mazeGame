import sys

import pygame
from pygame.locals import QUIT


class MazeGame():
	def __init__(self,title):
		self.screenWidth = 800
		self.screenHeigh = 600
		self.title = title
	def init(self):
		# 初始化
		pygame.init()
		window_surface = pygame.display.set_mode((self.screenWidth, self.screenHeigh))
		pygame.display.set_caption(self.title)
		window_surface.fill((255, 255, 255))

		fontStyle = pygame.font.SysFont('微軟正黑體', 20)
		text_surface = fontStyle.render('Hello World!', True, (0, 0, 0))

		window_surface.blit(text_surface, (100, 10))

		pygame.display.update()

		while True:
		  for event in pygame.event.get():
		    if event.type == QUIT:
		      pygame.quit()
		      sys.exit()

a = MazeGame("aasd")
a.init()
