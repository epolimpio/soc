#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
import sandpile

nx = 20
ny = 20
grain_number = 10000

pile = sandpile.sandpile2D(nx, ny)
plt.ion()

fig0 = plt.figure()
fig1 = plt.figure()
ax0 = fig0.add_subplot(1,1,1)
ax1 = fig1.add_subplot(1,1,1)

cplt1 = ax1.imshow(pile.z, interpolation = 'none', cmap = 'Oranges', vmax = 4, vmin = 0)
bar = plt.colorbar(cplt1, orientation = 'vertical')

for grain in range(grain_number):
	
	if (pile.throw_sand() > pile.z_critical):
		pile.avalanche()


	ax0.clear()
	cplt0 = ax0.imshow(pile.last_cluster.astype(int),  cmap='Greys', interpolation = 'none')
	#print pile.last_cluster.astype(int)
	plt.show()

	ax1.clear()
	cplt1 = ax1.imshow(pile.z, interpolation = 'none', cmap = 'Oranges', vmax = 4, vmin = 0)
	plt.draw()



