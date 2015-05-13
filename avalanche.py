import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from random import randint

class Avalanche2D:

	def __init__(self, nx, ny, movie = False,
		calc_slope_rule = 0, boundary = 0, slide_rule = 0):

		self.nx = nx
		self.ny = ny
		self.height_rule = height_rule
		self.boundary = boundary
		self.set_slide_rule(slide_rule)
		self.calc_slope_rule = calc_slope_rule
		self.movie = movie
		# The heights include the boundaries
		self.heights = np.zeros((ny+2, nx+2))
		self.slope = np.zeros((ny, nx))

	def calc_slope(self):

		if (self.calc_slope_rule == 0):

			self.slope = 4*self.heights[1:ny,1:nx] - (self.heights[1:ny,2:(nx+1)] +
							self.heights[2:(ny+1),1:nx] + self.heights[1:ny,0:(nx-1)] +
							self.heights[0:(ny-1),1:nx])

		else:

			self.slope = 2*self.heights[1:ny,1:nx] - (self.heights[1:ny,2:(nx+1)] +
							self.heights[2:(ny+1),1:nx])

		return self.slope

	def set_slide_rule(self, slide_rule):

		if slide_rule == 0:
			self.slide_rule = np.array([(1,0),(0,1)])
		elif slide_rule == 1:
			self.slide_rule = np.array([(1,0),(0,1),(1,1)])
		elif slide_rule == 2:
			self.slide_rule = np.array([(1,0),(0,1),(-1,0),(0,-1)])

		self.sands_to_slide = np.size(self.slide_rule, 0)

	def throw_sand(self):

		x = randint(1, self.nx)
		y = randint(1, self.ny)

		self.heights[y,x] = self.heights[y,x] + 1
		self.calc_slope()

		return self.heights[y,x], self.slope[y,x]

	def slide_sands(self, avalanche_spots):

		self.heights[avalanche_spots] = self.heights[avalanche_spots] - self.sands_to_slide
		sands_to_sum = avalanche_spots.astype(int)

		for i in range(self.sands_to_slide):

			add_sand = np.roll(np.roll(sum_array, self.slide_rule[i,1], axis = 0), 
								self.slide_rule[i,1], axis = 0)

			# We should do the boundary here !!!!
			
			self.heights = self.heights + add_sand


	def avalanche(self):

		t = 0
		s = 0



