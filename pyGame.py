import pygame
from pygame.locals import *
import sys
import pyautogui


class PyGame():
		def __init__(self):
			self.surface = pygame.display.set_mode((800,600))
			pygame.display.set_caption('Hello World:)')
			self.surface.fill((200, 255, 255))
			pygame.display.update()
			while True:
			# 迭代整個事件迴圈，若有符合事件則對應處理
				for event in pygame.event.get():
					# 當使用者結束視窗，程式也結束
					if event.type == QUIT:
						pygame.quit()
						sys.exit()