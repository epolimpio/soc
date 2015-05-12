import numpy as np
from random import randint

# Functions

class sandpile2D:

	def __init__(self, nx, ny, boundary = 0, z_critical = 4):

		self.nx = nx
		self.ny = ny
		self.boundary = boundary
		self.z_critical = z_critical
		self.z = np.zeros((ny, nx))

	def throw_sand(self):
		
		x = randint(0, self.nx-1)
		y = randint(0, self.ny-1)

		self.z[y,x] = self.z[y,x] + 1

		return self.z[y,x]

	def avalanche(self):

		t = 0
		s = 0

		cluster = np.zeros((self.ny, self.nx), dtype = bool)

		while (np.max(self.z) > self.z_critical):

			avalanche_spots = np.greater(self.z, self.z_critical)
			cluster = np.logical_or(cluster, avalanche_spots)

			s += np.sum(avalanche_spots)
			t += 1

			# Subtract the avalanche
			self.z[avalanche_spots] = self.z[avalanche_spots] - 4

			# Add to the neighbours, one by one
			# To this, we convert to a matrix of zeros and ones for summing
			sum_array = avalanche_spots.astype(int)

			# y + 1
			add_sand = np.roll(sum_array, 1, axis = 0)
			add_sand[0,:] = np.zeros(self.nx) # avoid the periodicity of roll func
			self.z = self.z + add_sand

			# y - 1
			add_sand = np.roll(sum_array, -1, axis = 0)
			add_sand[self.ny-1,:] = np.zeros(self.nx) # avoid the periodicity of roll func
			self.z = self.z + add_sand

			# x + 1			
			add_sand = np.roll(sum_array, 1, axis = 1)
			add_sand[:,0] = np.zeros(self.ny) # avoid the periodicity of roll func
			self.z = self.z + add_sand

			# x - 1
			add_sand = np.roll(sum_array, -1, axis = 1)
			add_sand[:,self.nx-1] = np.zeros(self.ny) # avoid the periodicity of roll func
			self.z = self.z + add_sand

		self.last_cluster = cluster

		return s, t




