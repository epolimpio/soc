#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
import avalanche

nx = 10
ny = 10
grain_number = 10000
sigma_critical = 16

pile = avalanche.avalanche2D(nx = nx, ny = ny, 
			sigma_critical = sigma_critical, slide_rule = 2, boundary = [1,1,1,1])
plt.ion()
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection='3d')
x_data, y_data = np.meshgrid( np.arange(pile.heights.shape[1]), np.arange(pile.heights.shape[0]))


for grain in range(grain_number):

	height, slope = pile.throw_sand()

	ax.clear()
	ax.grid(False)
	ax.view_init(azim = 180+45,elev = 70)
	surf = ax.plot_surface(x_data, y_data, pile.heights, rstride=1, cstride=1,
			cmap='Oranges',linewidth=0)
	#plt.axis('off')
	plt.draw()
	
	if (slope > pile.sigma_critical):
		pile.avalanche(critical_height = False)

