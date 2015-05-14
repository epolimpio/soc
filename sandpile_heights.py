#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
import avalanche

nx = 10
ny = 10
grain_number = 10000
sigma_critical = 20

pile = avalanche.avalanche2D(nx = nx, ny = ny, 
			sigma_critical = sigma_critical)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
#plt.ion()

sands_out = 0
for grain in range(grain_number):

	height, slope = pile.throw_sand()
	print height, slope

	data_array = pile.heights.copy()


	x_data, y_data = np.meshgrid( np.arange(data_array.shape[1]),
                              np.arange(data_array.shape[0]) )

	ax.clear()
	x_data = x_data.flatten()
	y_data = y_data.flatten()
	z_data = data_array.flatten()
	ax.bar3d(x_data,
          y_data,
          np.zeros(len(z_data)),
          1, 1, z_data)
	plt.show()
	
	if (slope > pile.sigma_critical):
		pile.avalanche(critical_height = False)

