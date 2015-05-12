#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import sandpile

nx = 10
ny = 10
grain_number = 1000

pile = sandpile.sandpile2D(nx, ny)
plt.ion()

#fig0 = plt.figure()
#fig1 = plt.figure()
#ax0 = fig0.add_subplot(1,1,1)
#ax1 = fig1.add_subplot(1,1,1)

#cplt1 = plt.imshow(pile.z, interpolation = 'none', cmap = 'Oranges', vmax = 4, vmin = 0)
#bar = plt.colorbar(cplt1, orientation = 'vertical')
for grain in range(grain_number):
	
	if (pile.throw_sand() > pile.z_critical):
		pile.avalanche()


	#ax0.clear()
	#cplt0 = plt.imshow(pile.last_cluster.astype(int),  cmap='Greys', interpolation = 'none')
	#plt.show()
	#ax1.clear()
	#cplt1 = plt.imshow(pile.z, interpolation = 'none', cmap = 'Oranges', vmax = 4, vmin = 0)
	#plt.draw()

