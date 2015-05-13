import copy
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from random import randint

# Functions

class sandpile2D:

	def __init__(self, nx, ny, slide_rule = 0, boundary = 0, sigma_critical = 3, movie = False):

		self.nx = nx
		self.ny = ny
		self.boundary = boundary
		self.sigma_critical = sigma_critical
		self.sigma = 0*np.ones((ny, nx))
		self.last_cluster = np.zeros((ny, nx), dtype=bool)

		self.movie = movie

		if movie:
			self.fig = plt.figure()
			self.ax = self.fig.add_subplot(1,1,1)
			self.biggest_cluster = 1

	def throw_sand(self):
		
		x = randint(0, self.nx-1)
		y = randint(0, self.ny-1)

		self.sigma[y,x] = self.sigma[y,x] + 1

		return self.sigma[y,x]

	def slide_to_all_directions(self, avalanche_spots):

		# Subtract the avalanche
		self.sigma[avalanche_spots] = self.sigma[avalanche_spots] - 4

		# Add to the neighbours, one by one
		# To this, we convert to a matrix of zeros and ones for summing
		sum_array = avalanche_spots.astype(int)

		# y + 1
		add_sand = np.roll(sum_array, 1, axis = 0)
		add_sand[0,:] = np.zeros(self.nx) # avoid the periodicity of roll func
		self.sigma = self.sigma + add_sand

		# y - 1
		add_sand = np.roll(sum_array, -1, axis = 0)
		add_sand[self.ny-1,:] = np.zeros(self.nx) # avoid the periodicity of roll func
		self.sigma = self.sigma + add_sand

		# x + 1			
		add_sand = np.roll(sum_array, 1, axis = 1)
		add_sand[:,0] = np.zeros(self.ny) # avoid the periodicity of roll func
		self.sigma = self.sigma + add_sand

		# x - 1
		add_sand = np.roll(sum_array, -1, axis = 1)
		add_sand[:,self.nx-1] = np.zeros(self.ny) # avoid the periodicity of roll func
		self.sigma = self.sigma + add_sand

	def avalanche(self):

		t = 0
		s = 0

		cluster = np.zeros((self.ny, self.nx), dtype = bool)

		if self.movie:
			clust_array = []
			plots = []

		while (np.max(self.sigma) > self.sigma_critical):

			avalanche_spots = np.greater(self.sigma, self.sigma_critical)
			cluster = np.logical_or(cluster, avalanche_spots)
			
			if self.movie:
				algo = copy.copy(self.sigma)
				algo[avalanche_spots] = algo[avalanche_spots] - 3*self.sigma_critical
				clust_array.append(-algo)

			s += np.sum(avalanche_spots)
			t += 1

			self.slide_to_all_directions(avalanche_spots)

		self.last_cluster = cluster
		
		if self.movie:
			clust_array.append(-copy.copy(self.sigma))

			if (np.sum(self.last_cluster) > self.biggest_cluster):
				self.biggest_cluster = np.sum(self.last_cluster)
				for pclust in clust_array:
					cplt0 = self.ax.imshow(pclust, interpolation = 'none', cmap = 'PuOr', vmax = self.sigma_critical, vmin = -self.sigma_critical)
					plots.append([cplt0])
				ani = animation.ArtistAnimation(self.fig, plots, interval = 300, blit = True)
				ani.save('biggest_cluster.mp4')

		return s, t

class sandpile3D:

	def __init__(self, nx, ny, nz, boundary = 0, sigma_critical = 7):

		self.nx = nx
		self.ny = ny
		self.nz = nz
		self.boundary = boundary
		self.sigma_critical = sigma_critical
		self.sigma = np.zeros((ny, nx, nz))

	def throw_sand(self):
		
		x = randint(0, self.nx-1)
		y = randint(0, self.ny-1)
		z = randint(0, self.nz-1)

		self.sigma[z,y,x] = self.sigma[z,y,x] + 1

		return self.sigma[z,y,x]

	def slide_to_all_directions(self, avalanche_spots):

		# Subtract the avalanche
		self.sigma[avalanche_spots] = self.sigma[avalanche_spots] - 6

		# Add to the neighbours, one by one
		# To this, we convert to a matrix of zeros and ones for summing
		sum_array = avalanche_spots.astype(int)

		# z + 1
		add_sand = np.roll(sum_array, 1, axis = 0)
		add_sand[0,:,:] = np.zeros(self.nx) # avoid the periodicity of roll func
		self.sigma = self.sigma + add_sand

		# z - 1
		add_sand = np.roll(sum_array, -1, axis = 0)
		add_sand[self.nz-1,:,:] = np.zeros(self.nx) # avoid the periodicity of roll func
		self.sigma = self.sigma + add_sand		

		# y + 1
		add_sand = np.roll(sum_array, 1, axis = 1)
		add_sand[:,0,:] = np.zeros(self.nx) # avoid the periodicity of roll func
		self.sigma = self.sigma + add_sand

		# y - 1
		add_sand = np.roll(sum_array, -1, axis = 1)
		add_sand[:,self.ny-1,:] = np.zeros(self.nx) # avoid the periodicity of roll func
		self.sigma = self.sigma + add_sand

		# x + 1			
		add_sand = np.roll(sum_array, 1, axis = 2)
		add_sand[:,:,0] = np.zeros(self.ny) # avoid the periodicity of roll func
		self.sigma = self.sigma + add_sand

		# x - 1
		add_sand = np.roll(sum_array, -1, axis = 2)
		add_sand[:,:,self.nx-1] = np.zeros(self.ny) # avoid the periodicity of roll func
		self.sigma = self.sigma + add_sand

	def avalanche(self):

		t = 0
		s = 0

		while (np.max(self.sigma) > self.sigma_critical):

			avalanche_spots = np.greater(self.sigma, self.sigma_critical)

			s += np.sum(avalanche_spots)
			t += 1

			self.slide_to_all_directions(avalanche_spots)

		return s, t