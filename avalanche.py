import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from random import randint

class Avalanche2D:

	def __init__(self, nx, ny, sigma_critical = 4, 
		calc_sigma_rule = 0, boundary = 0, slide_rule = 0):

		self.nx = nx
		self.ny = ny
		self.sigma_critical = sigma_critical
		self.height_rule = height_rule
		self.boundary = boundary
		self.slide_rule = slide_rule
		self.calc_sigma_rule = calc_sigma_rule
		# The heights include the boundaries
		self.heights = np.zeros((ny+2, nx+2))
		self.sigma = np.zeros((ny, nx))

	def calc_sigma(self):

		if (self.calc_sigma_rule == 0):

			self.sigma = 4*self.heights[1:ny,1:nx] - (self.heights[1:ny,2:(nx+1)] +
							self.heights[2:(ny+1),1:nx] + self.heights[1:ny,0:(nx-1)] +
							self.heights[0:(ny-1),1:nx])

		else:

			self.sigma = 2*self.heights[1:ny,1:nx] - (self.heights[1:ny,2:(nx+1)] +
							self.heights[2:(ny+1),1:nx])

		return self.sigma

	def set_slide_rule(self, slide_rule):

		if slide_rule == 0:
			self.slide_rule = np.array([(1,0),(0,1)])
		elif slide_rule == 1:
			self.slide_rule = np.array([(1,0),(0,1),(1,1)])
		elif slide_rule == 2:
			self.slide_rule = np.array([(1,0),(0,1),(-1,0),(0,-1)])