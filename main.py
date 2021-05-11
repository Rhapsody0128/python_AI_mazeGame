from maze import Maze
from walker import Walker,Drawer
import sys
import pygame as pg
from pygame.locals import QUIT
import random
import tkinter as tk







class MazeGame():
	def __init__(self):
		pg.init()
		
		screen = pg.display.set_mode((800,800))
		pg.display.set_caption("Maze Game")
		screen.fill((0,0,0))

		self.maze = Maze(3,screen)
		clock = pg.time.Clock()
		self.drawer = Drawer("Drawer",self.maze)

		while True:
			clock.tick(2)
			pg.display.update()
			if self.drawer.judgeArrivedGoal() == False:
				self.drawer.walk()
				self.maze.updateAllWall()
				if self.drawer.blocked > 6:
					self.drawer.position = self.maze.start.position
					
			for event in pg.event.get():
				if event.type == QUIT:
					pg.quit()
					sys.exit()



b = MazeGame()