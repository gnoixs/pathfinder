import pygame

from colors import *

class Cell:
	def __init__(self, row, col, width, total_rows):
		self.row = row
		self.col = col
		self.width = width
		self.total_rows = total_rows
		self.x = row * width
		self.y = col * width
		self.color = WHITE
		self.neighbors = []

	def get_pos(self):
		return self.row, self.col

	def is_closed(self):
		return self.color == ORANGE

	def is_open(self):
		return self.color == BLUE

	def is_barrier(self):
		return self.color == BLACK

	def is_start(self):
		return self.color == GREEN

	def is_end(self):
		return self.color == RED

	def reset(self):
		self.color = WHITE

	def make_start(self):
		self.color = GREEN

	def make_closed(self):
		self.color = ORANGE

	def make_open(self):
		self.color = BLUE

	def make_barrier(self):
		self.color = BLACK

	def make_end(self):
		self.color = RED

	def make_path(self):
		self.color = VIOLET

	def draw(self, win):
		pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

	def update_neighbors(self, grid):
		self.neighbors = []
		if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_barrier(): # DOWN
			self.neighbors.append(grid[self.row + 1][self.col])

		if self.row > 0 and not grid[self.row - 1][self.col].is_barrier(): # UP
			self.neighbors.append(grid[self.row - 1][self.col])

		if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_barrier(): # RIGHT
			self.neighbors.append(grid[self.row][self.col + 1])

		if self.col > 0 and not grid[self.row][self.col - 1].is_barrier(): # LEFT
			self.neighbors.append(grid[self.row][self.col - 1])

	def __lt__(self, other):
		return False