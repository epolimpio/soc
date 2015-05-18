#!/usr/bin/python

# This calculate the relevant distributions
# Using the class avalanche.py

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
import avalanche

nx = 50
ny = 50
grain_number = 2500000
sigma_critical = 2
slide_rule = 0
if slide_rule == 2:
	calc_slope_rule = 0
else:
	calc_slope_rule = 1
file_out = 'data/distheight'+str(nx)+str(ny)+str(slide_rule)+'.npz'

pile = avalanche.avalanche2D(nx = nx, ny = ny, calc_slope_rule = calc_slope_rule,
			sigma_critical = sigma_critical, slide_rule = slide_rule, boundary = [0,0,0,0])

dist_t = dict()
dist_s = dict()
dist_sand_out = dict()

n_avalanche = 0

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
#ax.axis('off')
x_data, y_data = np.meshgrid(np.arange(pile.heights.shape[1]),
				np.arange(pile.heights.shape[0]))
heights_array = []

for grain in range(grain_number):

	height, slope = pile.throw_sand()
	
	if (slope > pile.sigma_critical):
		n_avalanche += 1
		s, t, sands_out = pile.avalanche(critical_height = False)
		
		# Write distribution to histogram
		if s in dist_s:
			dist_s[s] += 1
		else:
			dist_s[s] = 1

		if t in dist_t:
			dist_t[t] += (1.0*s)/t
		else:
			dist_t[t] = (1.0*s)/t

		if sands_out in dist_sand_out:
			dist_sand_out[sands_out] += 1
		else:
			dist_sand_out[sands_out] = 1		


	if 20*(grain+1) % grain_number == 0:
		print str(100*(grain+1)/grain_number) + '%'

np.savez(file_out, np.array(dist_s.keys()), (1.0*np.array(dist_s.values()))/n_avalanche,
	np.array(dist_t.keys()), np.array(dist_t.values())/n_avalanche, 
	np.array(dist_sand_out.keys()), (1.0*np.array(dist_sand_out.values()))/n_avalanche)

ax.grid(False)
ax.view_init(azim = 45,elev = 70)
surf = ax.plot_surface(x_data, y_data, pile.heights, rstride=1, cstride=1,
		cmap='Oranges',linewidth=0)
plt.show()