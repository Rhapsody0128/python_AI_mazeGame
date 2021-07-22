from maze import Maze
from walker import AIWalker, Walker,Drawer
import sys
import pygame as pg
from pygame.locals import QUIT
import random
import tkinter as tk

class MazeGame():
	def __init__(self):
		pg.init()
		
		self.screenSize = 1000

		self.screen = pg.display.set_mode((self.screenSize,self.screenSize))
		pg.display.set_caption("Maze Game")
		self.screen.fill((0,0,0))

		self.maze = Maze(4,self.screen)
		clock = pg.time.Clock()
		self.drawer = Drawer("Drawer",self.maze)
		self.drawer.autoWalk()

		self.number = 0
		self.AIWalker = AIWalker(str(self.number),self.maze,None)

		self.font = pg.font.Font('freesansbold.ttf',18)
		self.textSurfaceObj = self.font.render('',True,(200,50,50))
		self.textRectObj = self.textSurfaceObj.get_rect()
		self.textRectObj.center=(self.screenSize-280,50+self.number)
		self.screen.blit(self.textSurfaceObj,self.textRectObj)
		self.datas = []
		

		while True:
			text = "*No."+self.AIWalker.name+"/*Move:"+str(self.AIWalker.step)+"/*Action"+str(self.AIWalker.motion)
			self.textSurfaceObj = self.font.render(text,True,(200,50,50))
			self.screen.blit(self.textSurfaceObj,self.textRectObj)
			for data in self.datas:
				self.screen.blit(data[0],data[1])
			

			clock.tick(200)
			pg.display.update()
			self.AIWalker.walk()
			
			self.maze.updateAllWall()
			for event in pg.event.get():
				if event.type == QUIT:
					pg.quit()
					sys.exit()
				elif event.type == pg.KEYDOWN:
					if event.key == pg.K_SPACE:
						self.number += 1
						self.saveData()
						self.screen.blit(self.textSurfaceObj,self.textRectObj)
						# textSurfaceObj = font.render('zxczxc',True,(200,50,50))
						# self.maze.clearVisit()
						self.AIWalker = AIWalker(str(self.number),self.AIWalker.maze,self.AIWalker.Qtable)
	def saveData(self):
		self.datas.append([self.textSurfaceObj,self.textRectObj])
		self.textSurfaceObj = self.font.render('',True,(200,50,50))
		self.textRectObj = self.textSurfaceObj.get_rect()
		self.textRectObj.center=(self.screenSize-280,50+self.number*20)
b = MazeGame()