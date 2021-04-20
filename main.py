import sys

from maze import Maze
from walker import Walker,Drawer
import random

import matplotlib.pyplot as plt



class MazeGame():
	def __init__(self):
		maze = Maze(7)
		player = Drawer("Drawer",maze)
		maze.drawMaze()
		

b = MazeGame()