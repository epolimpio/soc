import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from random import randint

class avalanche2D:

	def __init__(self, nx, ny, movie = False, sigma_critical = 6,
		calc_slope_rule = 0, boundary = [0,0,0,0], slide_rule = 2):

		self.nx = nx
		self.ny = ny

		self.boundary = boundary
		self.sigma_critical = sigma_critical
		self.set_boundary_bool()
		self.set_slide_rule(slide_rule)
		self.calc_slope_rule = calc_slope_rule
		self.movie = movie
		# The heights include the boundaries
		self.heights = np.zeros((ny+2, nx+2))
		self.slope = np.zeros((ny, nx))

	def set_slide_rule(self, slide_rule):

		if slide_rule == 0:
			self.slide_rule = np.array([(1,0),(0,1)])
		elif slide_rule == 1:
			self.slide_rule = np.array([(1,0),(0,1),(1,1)])
		elif slide_rule == 2:
			self.slide_rule = np.array([(1,0),(0,1),(-1,0),(0,-1)])

		self.sands_to_slide = np.size(self.slide_rule, 0)

	def set_boundary_bool(self):

		self.boundary_bool = np.zeros((4,self.ny+2, self.nx+2), dtype = bool)

		self.boundary_bool[0,:,0] = np.ones(self.ny+2, dtype = bool) # Left Boundary
		self.boundary_bool[1,0,:] = np.ones(self.nx+2, dtype = bool) # Bottom Boundary
		self.boundary_bool[2,:,self.nx+1] = np.ones(self.ny+2, dtype = bool) # Right Boundary
		self.boundary_bool[3,self.ny+1,:] = np.ones(self.nx+2, dtype = bool) # Upper Boundary

		self.all_boundaries = np.lib.pad(np.zeros((self.ny, self.nx)),
				(1,1), 'constant', constant_values = 1).astype(bool)


	def calc_slope(self):


		if (self.calc_slope_rule == 0):

			slope = 4*self.heights[1:(self.ny+1),1:(self.nx+1)] - (self.heights[1:(self.ny+1),2:(self.nx+2)] +
							self.heights[2:(self.ny+2),1:(self.nx+1)] + self.heights[1:(self.ny+1),0:self.nx] +
							self.heights[0:self.ny,1:(self.nx+1)])

		else:

			slope = 2*self.heights[1:(self.ny+1),1:(self.nx+1)] - (self.heights[1:(self.ny+1),2:(self.nx+2)] +
							self.heights[2:(self.ny+2),1:(self.nx+1)])

		return slope

	def throw_sand(self):

		x = randint(1, self.nx)
		y = randint(1, self.ny)

		self.heights[y,x] = self.heights[y,x] + 1
		self.slope = self.calc_slope()

		print self.heights
		print self.slope

		return self.heights[y,x], self.slope[y-1,x-1]

	def slide_sands(self, avalanche_spots):

		print avalanche_spots

		self.heights[avalanche_spots] = self.heights[avalanche_spots] - self.sands_to_slide
		sands_to_sum = avalanche_spots.astype(int)

		sands_out = 0

		for i in range(self.sands_to_slide):

			add_sand = np.roll(np.roll(sands_to_sum, self.slide_rule[i,1], axis = 0), 
								self.slide_rule[i,0], axis = 1)
			
			# Do the boundaries
			j = 0
			for bound_on in self.boundary:
				in_boundary = self.boundary_bool[j,:,:]
				if bound_on == 0:
					sands_out += np.sum(add_sand[in_boundary])
				else:
					roll_back = np.zeros((self.ny+2, self.nx+2))
					roll_back[in_boundary] = add_sand[in_boundary]
					roll_back = np.roll(np.roll(roll_back, -self.slide_rule[i,1], axis = 0), 
								-self.slide_rule[i,0], axis = 1)
					self.heights = self.heights + roll_back
				j += 1

			# We want the height at the boundary to keep at zero
			add_sand[self.all_boundaries] = 0
			
			self.heights = self.heights + add_sand
			self.slope = self.calc_slope()

		return sands_out

	def avalanche(self, critical_height = False):

		t = 0
		s = 0
		total_sands_out = 0

		cluster = np.zeros((self.ny+2, self.nx+2), dtype = bool)

		if self.movie:
			clust_array = []
			plots = []

		# boolean array to se where is more than the critical sigma
		if critical_height:
			avalanche_spots = np.greater(self.heights, self.sigma_critical)
		else:
			avalanche_spots = np.lib.pad(np.greater(self.slope, self.sigma_critical),
								(1,1), 'constant', constant_values = False)

		sum_spots = np.sum(avalanche_spots)

		while (sum_spots > 0):
			# boolean array with the complete the cluster
			cluster = np.logical_or(cluster, avalanche_spots)
			
			if self.movie:
				# save the sigma to later plot it and make a movie
				sigma_copy = copy.copy(self.sigma)
				# to point out where the avalanche is and differentiate when plotting
				sigma_copy[avalanche_spots] = sigma_copy[avalanche_spots] - 3*self.sigma_critical
				clust_array.append(-sigma_copy)

			s += sum_spots
			t += 1

			sands_out = self.slide_sands(avalanche_spots)
			total_sands_out += sands_out

			if critical_height:
				avalanche_spots = np.greater(self.heights, self.sigma_critical)
			else:
				avalanche_spots = np.lib.pad(np.greater(self.slope, self.sigma_critical),
									(1,1), 'constant', constant_values = False)

			sum_spots = np.sum(avalanche_spots)

		self.last_cluster = cluster
		
		if self.movie:
			clust_array.append(-copy.copy(self.sigma))

			if (np.sum(self.last_cluster) > self.biggest_cluster):
				self.biggest_cluster = np.sum(self.last_cluster)
				# plot all the different sigmas and append them to make the movie
				for pclust in clust_array:
					cplt0 = self.ax.imshow(pclust, interpolation = 'none', cmap = 'PuOr',
						vmax = self.sigma_critical, vmin = -self.sigma_critical)
					plots.append([cplt0])
				ani = animation.ArtistAnimation(self.fig, plots, interval = 50, blit = True)
				ani.save('biggest_cluster.mp4')

		return s, t, sands_out



