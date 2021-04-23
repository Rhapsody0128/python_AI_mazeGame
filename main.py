from maze import Maze
from walker import Walker,Drawer
from pyGame import PyGame
import random




class MazeGame():
	def __init__(self):
		pyGame = PyGame()
		maze = Maze(3,PyGame)
		player = Drawer("Drawer",maze,PyGame)
		maze.show()
		self.pyGmaeInit()



b = MazeGame()